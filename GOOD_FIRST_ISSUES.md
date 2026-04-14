# Good First Issues — SportMind

**Curated contribution opportunities matched to your skill level and available time.**

Every item here is specific, scoped, and has a clear definition of done.
Read `FIRST-RECORD-CHALLENGE.md` first — calibration records require no coding
and take 30 minutes. Everything below is for contributors who want to go deeper.

---

## ⭐ Level 1 — No coding required, 30-60 minutes

### 1A — Submit a calibration record (highest impact)

Run a SportMind analysis before a real match. Record the outcome. Submit.

**Why it matters:** All 126 current records were submitted by the founding team.
The first external record changes the evidence foundation.

**Full guide:** `FIRST-RECORD-CHALLENGE.md`

**Highest-priority sports right now:**

| Sport | Modifier | Records at threshold | Notes |
|---|---|---|---|
| Football (standard match) | `athlete_modifier` | 15 more needed | Non-derby, non-high-stakes only |
| Cricket (evening T20) | `dew_factor` | 45 more needed | IPL, PSL, BBL night matches |
| Netball | any | 3+ needed | Currently ZERO records |
| Rowing | any | 3+ needed | Currently ZERO records |
| Football | `derby_active` | 48 more needed | Any domestic derby |

---

### 1B — Fix a stale document reference

Find a document with an outdated version number, record count, or file count.
Fix it. Submit a PR with label `docs-fix`.

**Known stale references:**
- `community/leaderboard.md` — references v3.2 first entries; now at v3.65
- `README.md` badge — verify it shows current record count (126 records, 96% accuracy)
- Any document citing stale file counts (now 552 files)
- Any document citing record counts below 126 (current count is 126 across 21 sports)

---

### 1C — Translate a skill into your language

Translate a sport domain or athlete skill into a language SportMind does not yet cover.

**Current coverage:** AR, DE, ES, FR, HI, JA, PT

**Highest-value gaps:**
- Korean (KR): K-League, KBO baseball, esports
- Italian (IT): Serie A, MotoGP
- Turkish (TR): Süper Lig, basketball (Fenerbahçe/Galatasaray)
- Mandarin (ZH): CBA basketball, Chinese Super League

**Template:** Any existing i18n file (e.g., `i18n/de/sports/football/sport-domain-football.md`)

**Rule:** All field names, metrics, and code stay in English. Only explanatory prose translates.

**Label:** `i18n`

---

## ⭐⭐ Level 2 — Domain knowledge, 1-3 hours

### 2A — Expand a community stub sport (14 available)

These 14 sports exist as 20-line stubs. Each needs expansion to 150+ lines.

| Sport | File | Key market | Signal notes |
|---|---|---|---|
| Badminton | `sports/badminton/` | SE Asia, India, China | BWF World Championships; Olympic cycle |
| Volleyball | `sports/volleyball/` | Brazil, Italy, Japan | FIVB; indoor vs beach are separate |
| Table Tennis | `sports/table-tennis/` | China, Germany | ITTF World Tour; Olympic dominant |
| Field Hockey | `sports/field-hockey/` | Netherlands, India | FIH Pro League |
| Curling | `sports/curling/` | Canada, Scotland | World Championship; Olympic |
| Sailing | `sports/sailing/` | UK, Australia | America's Cup; Olympic classes |
| Squash | `sports/squash/` | Egypt, UK, Pakistan | PSA World Tour |
| Gymnastics | `sports/gymnastics/` | Russia, USA, China | Olympic cycle dominant |
| Judo | `sports/judo/` | Japan, France | IJF World Tour; Olympic |
| Triathlon | `sports/triathlon/` | UK, France, Australia | World Series; Ironman different |
| Weightlifting | `sports/weightlifting/` | China, Kazakhstan | IWF; Olympic |
| Swimming (open water) | `sports/swimming-open-water/` | Global | Differs from pool — conditions matter more |
| Taekwondo | `sports/taekwondo/` | South Korea | WT World Championship; Olympic |
| Fencing | `sports/fencing/` | France, Italy, Hungary | FIE World Championship; Olympic |

**Template:** `sports/netball/sport-domain-netball.md` — same required sections.

**Required sections:** Overview · Domain Model · Sport-Specific Risk Variables ·
Event Playbooks · Agent Reasoning Prompts · Signal Weight Adjustments · Compatibility

**Definition of done:** 150+ lines, passes `scripts/skill-validator.py`, label `new-sport`.

---

### 2B — Athlete intelligence skill for a stub sport

Build `athlete/athlete-intel-{sport}.md` for any sport that has a domain skill but no athlete file.

**Available:** All 14 stub sports above.

**Template:** `athlete/netball/athlete-intel-netball.md` (THIN depth — achievable in 2-3h)

**Required:** `get_athlete_signal_modifier` command, modifier reference table, integration workflow.

**Definition of done:** 150+ lines, validated, label `new-athlete-skill`.

---

### 2C — Submit 5+ calibration records for a single modifier

Five records for one modifier is the fastest path to threshold impact.
Five records from one contributor earns Senior Calibrator status in `community/CONTRIBUTORS.md`
and a named credit in the next recalibration report.

**Most needed (by modifier gap to threshold):**

| Modifier | Records needed | What to submit |
|---|---|---|
| `dew_factor` | 45 | IPL/PSL/BBL evening T20 matches |
| `derby_active` | 48 | Any domestic football derby |
| `competition_tier_weight` | 46 | UCL group stage vs knockout matches |
| `qualifying_delta_modifier` (F1) | 47 | Any F1 qualifying + race weekend |
| `athlete_modifier` (football, standard) | 15 | Non-derby, non-high-stakes EPL/La Liga/Serie A |

**Label:** `calibration-record`

---

## ⭐⭐⭐ Level 3 — Technical, 3-8 hours

### 3A — TypeScript starter pack example

All seven starter pack examples are Python. Build a TypeScript version of
`examples/starter-pack/03-single-sport-agent.py`.

**Stack:** TypeScript + fetch. Node.js 18+. No framework required.

**Output:** `examples/starter-pack/03-ts-single-sport-agent.ts` + README update.

**Label:** `typescript` + `starter-pack`

---

### 3B — Live calibration record validator script

A Python script that validates a submitted calibration record against the
official result from a public sports API.

**Input:** Calibration record JSON path.
**Output:** `VALIDATED` / `DISCREPANCY` / `UNVERIFIABLE`

**Data sources:** football-data.org (football) · ESPN API (NBA/NFL/NHL) · Cricinfo (cricket)

**Output:** `community/calibration-data/CONTRIBUTING.md`

**Label:** `tooling`

---

### 3C — Expand netball or rowing to GOOD depth

Both sports are THIN (~177 lines). GOOD depth = 220+ lines with full modifier suite.

**Required additions:** Full command set (6+ commands), competition-specific intelligence,
championship cycle, national ATM premiums, complete modifier reference table.

**Label:** `athlete-depth`

---

## ⭐⭐⭐⭐ Level 4 — Significant, 8+ hours

### 4A — External recalibration analysis

Submit 10+ calibration records for a single modifier, then write a mini-recalibration
report documenting what your records show. Format: `core/modifier-recalibration-v6.md`.

This would be the first external recalibration in the library's history.
You become the first external voice in SportMind's modifier calibration methodology.

**Recognition:** Named as author in the document. Permanent Calibration Pioneer credit.

---

### 4B — Hosted MCP server endpoint

Deploy a publicly accessible SportMind MCP server. Free-tier hosting acceptable.
Must stay live 6+ months. Guide: `platform/sportmind-mcp-deployment.md`.

**Label:** `infrastructure`

---

## How to claim

1. Open a GitHub issue: "Working on [issue name]"
2. Maintainer acknowledges within 48h — reserved for 14 days
3. Submit PR linking to the issue
4. Validator runs automatically; review within 7 days

**Labels:** `calibration-record` · `docs-fix` · `i18n` · `new-sport` ·
`new-athlete-skill` · `athlete-depth` · `tooling` · `typescript`

---

*MIT License · SportMind · sportmind.dev*
*`FIRST-RECORD-CHALLENGE.md` — fastest path to contributing*
*`community/calibration-data/CONTRIBUTING.md` — calibration record submission*
