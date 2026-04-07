# SportMind MCP — Live Deployment Guide

**How to deploy SportMind as a live, queryable MCP endpoint accessible to any
Claude instance or MCP-compatible agent framework.**

The local MCP server in `scripts/sportmind_mcp.py` works for Claude Desktop on
a single machine. This guide covers hosting SportMind as a shared endpoint —
so that any agent, anywhere, can call SportMind tools without running a local server.

---

## Deployment options

Three deployment patterns, ordered by complexity:

| Option | Best for | Cost | Setup time |
|---|---|---|---|
| GitHub Pages (static API) | Skill content serving; team sharing | Free | 15 minutes |
| Vercel/Render (live MCP) | Full MCP tool support; production use | Free tier available | 30 minutes |
| Docker (self-hosted) | Enterprise; full control; air-gapped | Infrastructure cost | 45 minutes |

---

## Option 1 — GitHub Pages (static skill serving)

GitHub Pages serves the SportMind skill files as static JSON/Markdown, making
them accessible to any agent via HTTP. This is not a full MCP server — it
does not support tool calls. It is a live, versioned skill content endpoint.

### Setup

```bash
# 1. Fork or clone the SportMind repository
git clone https://github.com/your-org/sportmind
cd sportmind

# 2. Create GitHub Pages deployment branch
git checkout -b gh-pages
mkdir -p _site

# 3. Generate the static API index
python3 scripts/generate_static_api.py  # see script below

# 4. Configure GitHub Pages
# In repository Settings → Pages → Source: gh-pages branch

# 5. Your SportMind endpoint:
# https://your-org.github.io/sportmind/api/v3/stack?sport=football
```

### Static API generator script

```python
# scripts/generate_static_api.py
"""
Generates static JSON files for GitHub Pages deployment.
Run before pushing to gh-pages branch.
"""
import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUTPUT = ROOT / "_site" / "api" / "v3"
OUTPUT.mkdir(parents=True, exist_ok=True)

SPORTS = [
    "football","basketball","cricket","mma","formula1","tennis",
    "rugby","rugby-league","afl","baseball","ice-hockey","motogp",
    "nascar","kabaddi","netball","handball","esports"
]

USE_CASES = ["fan_token_tier1","fan_token_tier2","prediction_market",
             "commercial_brief","pre_match","governance"]

def get_stack_files(sport: str, use_case: str) -> list:
    slug = sport.replace("_","-")
    files = []
    for path in [
        ROOT / "macro" / "macro-overview.md",
        ROOT / "market" / f"market-{slug}.md",
        ROOT / "sports" / slug / f"sport-domain-{slug}.md",
    ]:
        if path.exists(): files.append(path)
    
    athlete_dir = ROOT / "athlete" / slug
    if athlete_dir.exists():
        files.extend(sorted(athlete_dir.glob("athlete-intel-*.md")))
    
    if use_case in ("fan_token_tier1","fan_token_tier2","governance"):
        bridge_dir = ROOT / "fan-token" / f"{slug}-token-intelligence"
        if bridge_dir.exists():
            files.extend(sorted(bridge_dir.glob("*.md")))
    
    return files

# Generate stack files for each sport/use_case combination
for sport in SPORTS:
    for use_case in USE_CASES:
        files = get_stack_files(sport, use_case)
        stack = []
        for f in files:
            content = f.read_text(encoding="utf-8")
            stack.append({
                "skill_id": str(f.relative_to(ROOT)),
                "content":  content,
                "sha256":   hashlib.sha256(content.encode()).hexdigest(),
                "size_chars": len(content)
            })
        
        output_file = OUTPUT / f"stack-{sport}-{use_case}.json"
        with open(output_file, "w") as f:
            json.dump({
                "sport": sport,
                "use_case": use_case,
                "version": "3.15.0",
                "total_files": len(stack),
                "stack": stack,
                "loading_order": "macro → market → domain → athlete → fan-token"
            }, f, indent=2)

# Generate macro state endpoint
import shutil
shutil.copy(ROOT / "platform" / "macro-state.json",
            OUTPUT / "macro-state.json")

# Generate skill index
index = {
    "version": "3.15.0",
    "sports": SPORTS,
    "use_cases": USE_CASES,
    "total_skill_files": sum(1 for _ in ROOT.rglob("*.md") if ".git" not in str(_)),
    "endpoints": {
        "stack": "/api/v3/stack-{sport}-{use_case}.json",
        "macro": "/api/v3/macro-state.json",
        "hashes": "/api/v3/skill-hashes.json"
    }
}
with open(OUTPUT / "index.json", "w") as f:
    json.dump(index, f, indent=2)

print(f"Generated {len(SPORTS) * len(USE_CASES)} stack files + index")
```

### Using the GitHub Pages endpoint

```python
# Fetch SportMind stack from GitHub Pages
import requests, json

BASE_URL = "https://your-org.github.io/sportmind/api/v3"

def get_stack(sport: str, use_case: str = "pre_match") -> dict:
    url = f"{BASE_URL}/stack-{sport}-{use_case}.json"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

def get_macro() -> dict:
    response = requests.get(f"{BASE_URL}/macro-state.json", timeout=10)
    return response.json()

# Use in your agent
macro    = get_macro()
stack    = get_stack("football", "fan_token_tier1")
modifier = macro["macro_state"]["crypto_cycle"]["macro_modifier"]
```

---

## Option 2 — Vercel live MCP server (recommended for production)

Vercel's serverless functions host the full MCP server with HTTP/SSE transport,
enabling live tool calls from any Claude instance or MCP-compatible framework.

### Deploy to Vercel

```bash
# 1. Install Vercel CLI
npm install -g vercel

# 2. Create Vercel project structure
mkdir sportmind-mcp && cd sportmind-mcp
cp -r /path/to/sportmind/scripts/sportmind_mcp.py .
cp -r /path/to/sportmind/platform ./platform
cp -r /path/to/sportmind/sports ./sports
# ... copy all sportmind skill directories

# 3. Create Vercel serverless function
mkdir api
cat > api/mcp.py << 'EOF'
from http.server import BaseHTTPRequestHandler
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import SportMind MCP core
from sportmind_mcp import build_signal, get_macro_state, get_skill_files_for_stack
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = json.loads(self.rfile.read(content_length))
        
        method = body.get("method","")
        params = body.get("params",{})
        
        if method == "tools/call":
            name = params.get("name","")
            args = params.get("arguments",{})
            
            if name == "sportmind_signal":
                result = build_signal(
                    sport=args.get("sport","football"),
                    event_id=args.get("event_id",""),
                    use_case=args.get("use_case","pre_match"),
                    home_team=args.get("home_team",""),
                    away_team=args.get("away_team",""),
                    include_defi=args.get("include_defi_context",False)
                )
            elif name == "sportmind_macro":
                result = get_macro_state()
            else:
                result = {"error": f"Unknown tool: {name}"}
            
            response = {"result": {"content": [{"type":"text","text":json.dumps(result)}]}}
        else:
            response = {"error": "Method not supported"}
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

EOF

# 4. Deploy
vercel deploy --prod

# Your live MCP endpoint:
# https://sportmind-mcp.vercel.app/api/mcp
```

### Connect to Claude via Anthropic API

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=2000,
    mcp_servers=[
        {
            "type": "url",
            "url": "https://your-sportmind-mcp.vercel.app/api/mcp",
            "name": "sportmind"
        }
    ],
    messages=[{
        "role": "user",
        "content": "Analyse the UCL quarter-final PSG vs Arsenal tonight. Check macro state first."
    }]
)

print(response.content[0].text)
```

---

## Option 3 — Docker (self-hosted)

```dockerfile
# Dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY . .
RUN pip install mcp aiohttp --break-system-packages

EXPOSE 3001

CMD ["python", "scripts/sportmind_mcp.py", "--port", "3001"]
```

```bash
# Build and run
docker build -t sportmind-mcp .
docker run -p 3001:3001 sportmind-mcp

# Your local MCP endpoint:
# http://localhost:3001/mcp
```

---

## Keeping the live endpoint current

```python
# scripts/refresh_deployment.py
"""
Regenerate static API files and push to GitHub Pages.
Run after any SportMind library update.
"""
import subprocess, sys

def refresh():
    print("Regenerating static API...")
    result = subprocess.run(
        ["python3", "scripts/generate_static_api.py"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"ERROR: {result.stderr}")
        sys.exit(1)
    print(result.stdout)
    
    print("Regenerating hashes...")
    subprocess.run(
        ["python3", "scripts/security_validator.py", "--generate-hashes"],
        capture_output=True
    )
    
    print("Committing to gh-pages...")
    subprocess.run(["git", "add", "_site/"])
    subprocess.run(["git", "commit", "-m", f"Auto-deploy: v3.15.0"])
    subprocess.run(["git", "push", "origin", "gh-pages"])
    print("Done. Live endpoint updated.")

if __name__ == "__main__":
    refresh()
```

---

## Claude Desktop configuration (live endpoint)

```json
{
  "mcpServers": {
    "sportmind": {
      "type": "sse",
      "url": "https://your-sportmind-mcp.vercel.app/api/mcp",
      "description": "SportMind sports intelligence — live hosted endpoint"
    }
  }
}
```

For local development (still using stdio):
```json
{
  "mcpServers": {
    "sportmind-local": {
      "command": "python",
      "args": ["/path/to/sportmind/scripts/sportmind_mcp.py"]
    }
  }
}
```

---

## Endpoint security

```
PRODUCTION DEPLOYMENT SECURITY CHECKLIST:

[ ] Rate limiting: implement per-IP limits (recommended: 100 requests/hour)
[ ] Content hashing: verify skill-hashes.json on each deployment
[ ] HTTPS only: never serve MCP tools over plain HTTP
[ ] Input validation: reject unknown sport/use_case combinations
[ ] Macro state refresh: schedule update_macro_state.py every 6 hours
[ ] Monitoring: alert on error rate > 5% or latency > 2s
[ ] Skill file integrity: run security_validator.py before each deployment

See SECURITY.md for full security guidance including Threat 6 (prompt theft)
and Threat 7 (meta-injection) patterns for hosted deployments.
```

---

*MIT License · SportMind · sportmind.dev*
*See `platform/sportmind-mcp-server.md` for the full MCP tool specification.*
