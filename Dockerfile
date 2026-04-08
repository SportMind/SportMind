# SportMind MCP Server — Docker deployment
# Build:  docker build -t sportmind-mcp .
# Run:    docker run -p 3001:3001 sportmind-mcp
# Health: curl http://localhost:3001/health

FROM python:3.11-slim

WORKDIR /sportmind

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy library
COPY . .

# Expose MCP endpoint
EXPOSE 3001

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:3001/health')"

# Run HTTP/SSE server
CMD ["python", "scripts/sportmind_mcp.py", "--http", "--port", "3001"]
