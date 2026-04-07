# SportMind — LangChain / Python Integration

> **v2.1.0:** SportMind now has five layers. Full loading order:
> Layer 5 (macro) → Layer 4 (market) → Layer 1 (sport domain) → Layer 2 (athlete) → Layer 3 (fan token).
> The examples below show Layers 1–2. Prepend `macro/macro-overview.md` and
> `market/market-{sport}.md` for complete five-layer intelligence.

Load SportMind skills as tools, context documents, or retrieval sources
in LangChain, CrewAI, AutoGen, or any Python agent framework.

---

## Option A — Skills as context documents (simplest)

```python
from pathlib import Path

class SportMindSkill:
    """Load a SportMind skill as agent context."""

    def __init__(self, skill_path: str, base_dir: str = "."):
        skill_file = Path(base_dir) / skill_path.glob("sport-domain-*.md") or skill_path.glob("athlete-intel-*.md")
        if not skill_file.exists():
            raise FileNotFoundError(f"Skill not found: {skill_file}")
        self.content = skill_file.read_text()
        self.name = skill_path
        self.sport = skill_path.split("/")[-1]

    def as_system_context(self) -> str:
        return f"=== SPORTMIND: {self.name.upper()} ===\n{self.content}"


class SportMindCore:
    """Load SportMind core reference documents."""

    def __init__(self, base_dir: str = "."):
        self.base = Path(base_dir) / "core"

    def modifier_system(self) -> str:
        return (self.base / "core-athlete-modifier-system.md").read_text()

    def signal_weights(self) -> str:
        return (self.base / "core-signal-weights-by-sport.md").read_text()

    def result_matrices(self) -> str:
        return (self.base / "core-result-impact-matrices.md").read_text()


# Usage
sportmind_base = "/path/to/sportmind"

football_domain  = SportMindSkill("sports/football",  sportmind_base)
football_athlete = SportMindSkill("athlete/football", sportmind_base)
core             = SportMindCore(sportmind_base)

system_prompt = "\n\n".join([
    "You are a football sports intelligence agent.",
    football_domain.as_system_context(),
    football_athlete.as_system_context(),
    f"=== SPORTMIND: SIGNAL WEIGHTS ===\n{core.signal_weights()}",
    f"=== SPORTMIND: RESULT MATRICES ===\n{core.result_matrices()}",
])

print(f"System prompt length: {len(system_prompt)} chars")
```

---

## Option B — Skills as LangChain tools

```python
from langchain.tools import BaseTool
from langchain_anthropic import ChatAnthropic
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from pathlib import Path
from typing import Optional
import json

SPORTMIND_BASE = "/path/to/sportmind"

class GetSportSkillTool(BaseTool):
    name: str = "get_sport_skill"
    description: str = (
        "Load a SportMind sport domain skill. "
        "Provides domain model, event playbooks, risk variables, "
        "and agent reasoning prompts for a specific sport. "
        "Input: sport name (football, basketball, mma, esports, american-football)"
    )

    def _run(self, sport: str) -> str:
        skill_path = Path(SPORTMIND_BASE) / next(Path(SPORTMIND_BASE, "sports", sport).glob("sport-domain-*.md"))
        if not skill_path.exists():
            available = [d.name for d in (Path(SPORTMIND_BASE) / "sports").iterdir() if d.is_dir()]
            return f"Skill not found for '{sport}'. Available: {', '.join(available)}"
        return skill_path.read_text()


class GetAthleteSkillTool(BaseTool):
    name: str = "get_athlete_skill"
    description: str = (
        "Load a SportMind athlete intelligence skill. "
        "Provides player availability commands, form score system, "
        "and composite modifier pipeline for a specific sport. "
        "Input: sport name (football, mma, esports, nfl, nba, nhl, cricket, tennis, rugby) "
        "or 'meta' for the cross-sport orchestrator."
    )

    def _run(self, sport: str) -> str:
        skill_path = Path(SPORTMIND_BASE) / next(Path(SPORTMIND_BASE, "athlete", sport).glob("athlete-intel-*.md"))
        if not skill_path.exists():
            available = [d.name for d in (Path(SPORTMIND_BASE) / "athlete").iterdir() if d.is_dir()]
            return f"Athlete skill not found for '{sport}'. Available: {', '.join(available)}"
        return skill_path.read_text()


class GetSignalWeightsTool(BaseTool):
    name: str = "get_signal_weights"
    description: str = (
        "Get SportMind recommended signal weights for a specific sport. "
        "Returns how to weight market/whale, social, sports catalyst, "
        "price trend, and macro signals for that sport. "
        "Input: sport name"
    )

    def _run(self, sport: str) -> str:
        weights_path = Path(SPORTMIND_BASE) / "core" / "core-signal-weights-by-sport.md"
        content = weights_path.read_text()
        # Return full content — agent will extract sport-specific section
        return f"Requesting weights for sport: {sport}\n\n{content}"


class GetResultMatrixTool(BaseTool):
    name: str = "get_result_matrix"
    description: str = (
        "Get expected price/market impact ranges for different result types. "
        "Input: sport name"
    )

    def _run(self, sport: str) -> str:
        matrices_path = Path(SPORTMIND_BASE) / "core" / "core-result-impact-matrices.md"
        content = matrices_path.read_text()
        return f"Result impact data for: {sport}\n\n{content}"


class ApplyModifierTool(BaseTool):
    name: str = "apply_athlete_modifier"
    description: str = (
        "Compute an athlete modifier given player status data. "
        "Input: JSON string with keys: "
        "sport, key_players (list of {name, status, form_score}), "
        "fatigue_index (0-1), lineup_confirmed (bool), weather_modifier (0.87-1.0). "
        "Returns: composite_modifier, adjusted_signal_score, breakdown."
    )

    def _run(self, input_json: str) -> str:
        try:
            data = json.loads(input_json)
        except json.JSONDecodeError:
            return "Error: input must be valid JSON"

        # Simplified modifier computation
        # In production this would call the athlete skills API
        players = data.get("key_players", [])
        status_map = {"CONFIRMED": 1.05, "PROBABLE": 1.02, "DOUBT": 0.85, "OUT": 0.72}
        form_map = lambda f: 1.20 if f >= 85 else 1.10 if f >= 70 else 1.00 if f >= 55 else 0.92 if f >= 40 else 0.82

        # Average availability modifier across key players
        availability_mods = [status_map.get(p.get("status", "DOUBT"), 0.92) for p in players]
        form_mods         = [form_map(p.get("form_score", 65)) for p in players]

        avg_availability = sum(availability_mods) / len(availability_mods) if availability_mods else 1.0
        avg_form         = sum(form_mods)         / len(form_mods)         if form_mods         else 1.0

        fatigue   = data.get("fatigue_index", 0.5)
        fatigue_mod = 1.0 - (max(0, fatigue - 0.4) * 0.25)

        lineup_mod = 1.10 if data.get("lineup_confirmed") else 0.95
        weather_mod = data.get("weather_modifier", 1.0)

        composite = round(avg_availability * avg_form * fatigue_mod * lineup_mod * weather_mod, 3)
        composite = max(0.40, min(1.40, composite))

        base = data.get("base_signal_score", 65)
        adjusted = min(100, round(base * composite))
        direction = "BULLISH" if adjusted >= 68 else "NEUTRAL" if adjusted >= 52 else "BEARISH"

        return json.dumps({
            "composite_modifier": composite,
            "adjusted_signal_score": adjusted,
            "direction": direction,
            "breakdown": {
                "availability": round(avg_availability, 3),
                "form": round(avg_form, 3),
                "fatigue": round(fatigue_mod, 3),
                "lineup_confirmation": lineup_mod,
                "weather": weather_mod,
            },
            "recommendation": (
                f"{'Strong entry signal' if composite >= 1.10 else 'Consider entry' if composite >= 1.0 else 'Hold — wait for better conditions' if composite >= 0.90 else 'Skip — conditions unfavourable'}. "
                f"Adjusted score {adjusted} ({direction})."
            )
        }, indent=2)


# Build the agent
tools = [
    GetSportSkillTool(),
    GetAthleteSkillTool(),
    GetSignalWeightsTool(),
    GetResultMatrixTool(),
    ApplyModifierTool(),
]

llm = ChatAnthropic(model="claude-sonnet-4-6")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sports intelligence agent powered by SportMind. "
               "Use the SportMind tools to load domain knowledge before evaluating any event. "
               "Always load the sport domain skill AND athlete skill before giving a recommendation."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


# Example usage
if __name__ == "__main__":
    result = executor.invoke({
        "input": (
            "PSG are playing UCL tomorrow. "
            "Mbappé is confirmed starting with form score 91. "
            "Goalkeeper Donnarumma is also confirmed with form 78. "
            "One midfielder is DOUBT. "
            "Fatigue index is 0.42. Lineup confirmed. "
            "Base FTI signal score is 68. "
            "What is the SportMind adjusted recommendation?"
        )
    })
    print(result["output"])
```

---

## Option C — CrewAI multi-agent setup

```python
from crewai import Agent, Task, Crew
from crewai.tools import BaseTool

# Define SportMind-aware agents
domain_analyst = Agent(
    role="Sport Domain Analyst",
    goal="Interpret sporting events using SportMind domain models",
    backstory="Expert in sport-specific token and prediction market dynamics. "
              "Uses SportMind domain skills to assess match importance, competition context, "
              "and expected price impact ranges.",
    tools=[GetSportSkillTool(), GetResultMatrixTool(), GetSignalWeightsTool()],
    llm=ChatAnthropic(model="claude-sonnet-4-6"),
    verbose=True,
)

athlete_analyst = Agent(
    role="Athlete Intelligence Analyst",
    goal="Compute athlete modifiers and assess player-level impact on predictions",
    backstory="Specialist in player availability, form, and matchup analysis. "
              "Uses SportMind athlete skills to compute composite modifiers "
              "that adjust base signal scores.",
    tools=[GetAthleteSkillTool(), ApplyModifierTool()],
    llm=ChatAnthropic(model="claude-sonnet-4-6"),
    verbose=True,
)

signal_synthesiser = Agent(
    role="Signal Synthesiser",
    goal="Combine domain context, athlete modifier, and market signals into a final recommendation",
    backstory="Combines SportMind intelligence with live market data to produce "
              "an adjusted_signal_score and clear actionable recommendation.",
    tools=[],
    llm=ChatAnthropic(model="claude-sonnet-4-6"),
    verbose=True,
)

# Define the workflow
crew = Crew(
    agents=[domain_analyst, athlete_analyst, signal_synthesiser],
    tasks=[
        Task(
            description="Load the football domain skill and assess match importance for PSG vs Galatasaray (UCL)",
            agent=domain_analyst,
            expected_output="Match importance score, competition tier, and relevant playbook"
        ),
        Task(
            description="Compute the athlete modifier for PSG: Mbappé CONFIRMED (form 91), "
                        "Donnarumma CONFIRMED (form 78), one midfielder DOUBT. Fatigue 0.42. "
                        "Lineup confirmed. Base signal 68.",
            agent=athlete_analyst,
            expected_output="Composite modifier value with component breakdown"
        ),
        Task(
            description="Synthesise domain context and athlete modifier into final recommendation. "
                        "Whale sell_ratio is 0.685 (bracket 0.68-0.70, 75% historical WR).",
            agent=signal_synthesiser,
            expected_output="adjusted_signal_score, direction, confidence, recommendation"
        ),
    ],
    verbose=True,
)

result = crew.kickoff()
print(result)
```

---

## Environment setup

```bash
pip install langchain langchain-anthropic anthropic crewai

export ANTHROPIC_API_KEY="your-key-here"
```
