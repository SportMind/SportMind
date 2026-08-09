/**
 * SportMind Starter Pack — Example 03: Single Sport Agent (TypeScript)
 * =====================================================================
 * A complete football fan token monitoring agent.
 * TypeScript port of 03-single-sport-agent.py.
 *
 * What this demonstrates:
 *   - Class-based SportMind agent structure
 *   - Level 2 autonomy (acts when SMS >= 80, escalates otherwise)
 *   - Scheduled 4-hour monitoring cycle using recursive setTimeout
 *   - Alert generation with full reasoning trail
 *   - Graceful degradation when data is unavailable
 *
 * What you need:
 *   Node.js 18+ (fetch built-in — no framework required)
 *   npx ts-node 03-ts-single-sport-agent.ts
 *   node scripts/sportmind_api.js   # in another terminal
 *
 * What to change first:
 *   TOKEN_SYMBOL  — change to your token (BAR, CITY, JUV, etc.)
 *   SPORT         — change to your sport
 *   MIN_SMS       — your confidence threshold (default: 60)
 *   ALERT_WEBHOOK — your notification endpoint
 *
 * This agent:
 *   - Checks macro state every 4 hours
 *   - Detects upcoming football matches
 *   - Generates pre-match signals at T-48h and T-2h
 *   - Alerts when signal meets threshold
 *   - Escalates when confidence is insufficient
 */

// ── Configuration ─────────────────────────────────────────────────────────────

const TOKEN_SYMBOL: string   = "PSG";
const SPORT: string          = "football";
const CLUB_NAME: string      = "Paris Saint-Germain";
const USE_CASE: string       = "fan_token_tier1";
const SPORTMIND_API: string  = process.env.SPORTMIND_API ?? "http://localhost:8080";
const ALERT_WEBHOOK: string  = process.env.ALERT_WEBHOOK ?? "";
const MIN_SMS: number        = 60.0;   // Minimum SMS to recommend ENTER
const CYCLE_HOURS: number    = 4;      // How often to run the monitoring cycle
const AUTONOMY_LEVEL: number = 2;      // Level 2: acts at SMS >= MIN_SMS, escalates otherwise

// ── Logging helpers ───────────────────────────────────────────────────────────

function logInfo(msg: string): void {
  console.log(`${new Date().toISOString()} [sportmind.${TOKEN_SYMBOL.toLowerCase()}-agent] INFO: ${msg}`);
}

function logWarn(msg: string): void {
  console.warn(`${new Date().toISOString()} [sportmind.${TOKEN_SYMBOL.toLowerCase()}-agent] WARN: ${msg}`);
}

function logError(msg: string): void {
  console.error(`${new Date().toISOString()} [sportmind.${TOKEN_SYMBOL.toLowerCase()}-agent] ERROR: ${msg}`);
}

// ── Types ─────────────────────────────────────────────────────────────────────

interface UpcomingEvent {
  event_id:         string;
  home_team:        string;
  away_team:        string;
  hours_away:       number;
  competition:      string;
  competition_tier: string;
}

interface SignalFlags {
  lineup_unconfirmed:    boolean;
  macro_override_active: boolean;
  liquidity_warning:     boolean;
  liquidity_critical?:   boolean;
}

interface Signal {
  event_id:     string;
  window:       string;
  generated_at: string;
  signal: {
    direction:          string;
    adjusted_score:     number;
    confidence_tier:    string;
    recommended_action: string;
    position_size:      string;
  };
  sportmind_score: {
    sms:          number;
    sms_tier:     string;
    layers_loaded: number[];
  };
  modifiers: {
    macro_modifier: number;
    comp_weight:    number;
    composite:      number;
    flags:          SignalFlags;
  };
  token:      string;
  agent_note: string;
}

interface SkillFile {
  skill_id: string;
  [key: string]: unknown;
}

// ── The agent ─────────────────────────────────────────────────────────────────

/**
 * Single-sport SportMind agent for fan token monitoring.
 * Level 2 autonomy: generates recommendations autonomously; alerts operator.
 * Does NOT execute trades or financial actions — see core/autonomous-agent-framework.md.
 */
class PSGTokenAgent {
  private macroModifier: number    = 1.00;
  private macroPhase: string       = "UNKNOWN";
  private macroLastUpdated: Date | null = null;
  private cycleCount: number       = 0;
  private alertCount: number       = 0;
  private skillStack: SkillFile[]  = [];

  // ── Initialisation ──────────────────────────────────────────────────────────

  async initialise(): Promise<void> {
    logInfo(`Initialising ${TOKEN_SYMBOL} agent (Level ${AUTONOMY_LEVEL} autonomy)`);

    // Step 1: Load skill stack (Tier 0 — permanent, load once)
    await this.loadSkillStack();

    // Step 2: Fetch initial macro state
    await this.refreshMacro();

    logInfo(
      `Initialised. Stack: ${this.skillStack.length} files. ` +
      `Macro: ${this.macroPhase} (${this.macroModifier})`
    );
  }

  private async loadSkillStack(): Promise<void> {
    /** Load SportMind skill stack. Permanent content — load once per session. */
    try {
      const res = await fetch(
        `${SPORTMIND_API}/stack?sport=${encodeURIComponent(SPORT)}&use_case=${encodeURIComponent(USE_CASE)}`
      );
      const data = await res.json() as { stack?: SkillFile[] };
      this.skillStack = data.stack ?? [];
      logInfo(`Loaded ${this.skillStack.length} skill files`);
    } catch (e) {
      logError(`Could not load skill stack: ${e}`);
      this.skillStack = [];
    }
  }

  // ── Monitoring cycle ────────────────────────────────────────────────────────

  async runCycle(): Promise<void> {
    /** Main monitoring cycle — runs every CYCLE_HOURS hours. */
    this.cycleCount++;
    logInfo(`── Cycle ${this.cycleCount} ──────────────────────`);

    // Step 1: Refresh macro if stale (Tier 3 — daily)
    if (this.macroIsStale()) {
      await this.refreshMacro();
    }

    // Step 2: Check for upcoming matches
    const events = await this.getUpcomingEvents();

    for (const event of events) {
      await this.processEvent(event);
    }

    logInfo(`Cycle ${this.cycleCount} complete. Macro: ${this.macroPhase}`);
  }

  private async getUpcomingEvents(): Promise<UpcomingEvent[]> {
    /**
     * Detect upcoming events for this club.
     * In production: call your sports data API here.
     * This stub returns a simulated upcoming event for demonstration.
     */
    // REPLACE THIS with your live fixture data source:
    // e.g. football-data.org, Sportradar, your own database
    //
    // const res = await fetch(`https://your-api/fixtures?team=${encodeURIComponent(CLUB_NAME)}`);
    // const fixtures = await res.json() as UpcomingEvent[];
    // return fixtures.filter(f => f.hours_away > 0 && f.hours_away < 72);

    // Stub: simulated UCL match in 46 hours
    return [
      {
        event_id:         "ucl-qf-psg-arsenal-2026",
        home_team:        "PSG",
        away_team:        "Arsenal",
        hours_away:       46,
        competition:      "ucl_knockout",
        competition_tier: "TIER_1"
      }
    ];
  }

  private async processEvent(event: UpcomingEvent): Promise<void> {
    /** Process a single upcoming event through the SportMind reasoning chain. */
    const { event_id, hours_away } = event;
    const tier = event.competition_tier ?? "TIER_3";

    // Determine which analysis window we are in
    let window: string;
    if (hours_away <= 2) {
      window = "T-2h";
    } else if (hours_away <= 48) {
      window = "T-48h";
    } else {
      return; // Too far away; skip
    }

    logInfo(`[${event_id}] Processing ${window} signal (Tier: ${tier})`);

    // Generate signal
    const signal = await this.generateSignal(event, window);

    // Apply autonomy decision
    const sms = signal.sportmind_score.sms;

    if (this.shouldAct(signal)) {
      await this.sendAlert(signal, event, window);
      this.alertCount++;
    } else {
      await this.escalate(signal, event, window, `SMS ${sms} below threshold ${MIN_SMS}`);
    }
  }

  // ── Signal generation ───────────────────────────────────────────────────────

  private async generateSignal(event: UpcomingEvent, window: string): Promise<Signal> {
    /**
     * Generate SportMind signal using the six-step reasoning chain.
     * See core/reasoning-patterns.md for the full chain specification.
     */

    // STEP 1: Macro already loaded — apply modifier
    // STEP 2: Competition classification
    const compWeights: Record<string, number> = {
      ucl_final:         1.00,
      ucl_knockout:      0.75,
      league_decider:    0.65,
      league_standard:   0.35,
      domestic_cup:      0.50
    };
    const compWeight = compWeights[event.competition] ?? 0.35;

    // STEP 3: Athlete availability
    const lineupUnconfirmed = event.hours_away > 2;

    // STEP 4: Signal computation
    const baseScore     = 55.0; // Replace with your form model
    let adjustedScore   = Math.round(baseScore * this.macroModifier * compWeight / 0.35 * 10) / 10;
    adjustedScore       = Math.min(adjustedScore, 100.0);

    // STEP 5: DeFi context (if fan token application)
    // See platform/realtime-integration-patterns.md Pattern 3 for live TVL fetch
    const liquidityWarning = false; // Replace with live TVL check

    // STEP 6: SMS computation
    const layers = new Set<number>();
    for (const skill of this.skillStack) {
      const p = skill.skill_id ?? "";
      if (p.startsWith("macro"))        layers.add(5);
      else if (p.startsWith("market"))  layers.add(4);
      else if (p.startsWith("sports"))  layers.add(1);
      else if (p.startsWith("athlete")) layers.add(2);
      else if (p.startsWith("fan-token")) layers.add(3);
    }

    const sms = Math.round(
      (layers.size / 5) * 0.35 * 100 +
      (this.macroModifier >= 0.75 ? 1.0 : 0.6) * 0.25 * 100 +
      0.25 * 100 +
      Math.min(this.macroModifier, 1.0) * 0.15 * 100,
    );

    const smsTier =
      sms >= 80 ? "HIGH_QUALITY" :
      sms >= 60 ? "GOOD" :
      sms >= 40 ? "PARTIAL" :
      "INSUFFICIENT";

    const flags: SignalFlags = {
      lineup_unconfirmed:    lineupUnconfirmed,
      macro_override_active: this.macroModifier < 0.75,
      liquidity_warning:     liquidityWarning
    };

    // Position size recommendation
    const anyFlag = Object.values(flags).some(Boolean);
    const positionSize =
      anyFlag        ? "50%"  :
      sms >= 80      ? "100%" :
      sms >= 60      ? "65%"  :
      "WAIT";

    const direction = event.home_team === CLUB_NAME ? "HOME" : "AWAY";
    const recommendedAction =
      (sms >= MIN_SMS && !flags.macro_override_active) ? "ENTER" : "WAIT";

    return {
      event_id:     event.event_id,
      window,
      generated_at: new Date().toISOString(),
      signal: {
        direction,
        adjusted_score:     adjustedScore,
        confidence_tier:    sms >= 60 ? "MEDIUM" : "LOW",
        recommended_action: recommendedAction,
        position_size:      positionSize
      },
      sportmind_score: {
        sms,
        sms_tier:     smsTier,
        layers_loaded: [...layers].sort((a, b) => a - b)
      },
      modifiers: {
        macro_modifier: this.macroModifier,
        comp_weight:    compWeight,
        composite:      Math.round(this.macroModifier * compWeight * 1000) / 1000,
        flags
      },
      token:      TOKEN_SYMBOL,
      agent_note: (
        "SportMind intelligence — not financial advice. " +
        "Integrate live lineup and form data for full accuracy."
      )
    };
  }

  // ── Autonomy decision ───────────────────────────────────────────────────────

  private shouldAct(signal: Signal): boolean {
    /**
     * Level 2 autonomy decision: act autonomously or escalate?
     * Implements the Autonomous Action Matrix from core/autonomous-agent-framework.md.
     */
    const sms   = signal.sportmind_score.sms;
    const flags = signal.modifiers.flags;

    // Blocking flags are absolute — see Safety Principle 3
    if (flags.macro_override_active) return false;
    if (flags.liquidity_critical)    return false;

    // Confidence threshold
    return sms >= MIN_SMS;
  }

  // ── Actions ─────────────────────────────────────────────────────────────────

  private async sendAlert(signal: Signal, event: UpcomingEvent, window: string): Promise<void> {
    /** Send alert to operator. DOES NOT execute any financial action. */
    const sms    = signal.sportmind_score.sms;
    const action = signal.signal.recommended_action;
    const activeFlags = Object.entries(signal.modifiers.flags)
      .filter(([, v]) => v).map(([k]) => k);

    const message =
      `📊 ${TOKEN_SYMBOL} SIGNAL [${window}]\n` +
      `Event: ${event.home_team} vs ${event.away_team}\n` +
      `Action: ${action} | SMS: ${sms} (${signal.sportmind_score.sms_tier})\n` +
      `Macro: ${this.macroPhase} (${this.macroModifier})\n` +
      `Position size: ${signal.signal.position_size}\n` +
      `Flags: ${JSON.stringify(activeFlags)}`;

    logInfo(`ALERT: ${message}`);

    if (ALERT_WEBHOOK) {
      try {
        await fetch(ALERT_WEBHOOK, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ text: message, signal })
        });
      } catch (e) {
        logError(`Alert webhook failed: ${e}`);
      }
    }
  }

  private async escalate(
    signal: Signal,
    event: UpcomingEvent,
    window: string,
    reason: string
  ): Promise<void> {
    /**
     * Escalate to human review — Safety Principle 4 (escalation completeness).
     * Provides full reasoning trail, not just 'confidence too low'.
     */
    const sms   = signal.sportmind_score.sms;
    const flags = signal.modifiers.flags;
    const activeFlags = Object.entries(flags).filter(([, v]) => v).map(([k]) => k);

    const resolutions: string[] = [];
    if (flags.lineup_unconfirmed)    resolutions.push("lineup confirmation at T-2h");
    if (flags.macro_override_active) resolutions.push("macro improvement above 0.75");
    if (sms < MIN_SMS)               resolutions.push("additional skill data");

    const escalationBrief =
      `⚠️ ESCALATION REQUIRED [${window}]\n` +
      `Event: ${event.home_team} vs ${event.away_team}\n` +
      `Reason: ${reason}\n` +
      `SMS: ${sms} | Macro: ${this.macroPhase}\n` +
      `Active flags: ${activeFlags.length ? activeFlags.join(", ") : "none"}\n` +
      `What would resolve this: ${resolutions.join(", ") || "none"}`;

    logWarn(`ESCALATE: ${escalationBrief}`);

    if (ALERT_WEBHOOK) {
      try {
        await fetch(ALERT_WEBHOOK, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ text: escalationBrief, type: "escalation", signal })
        });
      } catch (e) {
        logError(`Escalation webhook failed: ${e}`);
      }
    }
  }

  // ── Macro management ─────────────────────────────────────────────────────────

  private async refreshMacro(): Promise<void> {
    /** Refresh macro state — Tier 3 (4-8 hour cycle). */
    try {
      const res  = await fetch(`${SPORTMIND_API}/macro-state`);
      const data = await res.json() as { macro_state: { crypto_cycle: { macro_modifier: number; phase: string } } };
      const cycle = data.macro_state.crypto_cycle;
      this.macroModifier     = cycle.macro_modifier;
      this.macroPhase        = cycle.phase;
      this.macroLastUpdated  = new Date();
      logInfo(`Macro refreshed: ${this.macroPhase} (${this.macroModifier})`);
    } catch (e) {
      logError(`Macro refresh failed — using last known state: ${e}`);
      // Graceful degradation: keep existing state, don't fail
    }
  }

  private macroIsStale(): boolean {
    /** Macro state is stale if > 8 hours old — see core/temporal-awareness.md. */
    if (!this.macroLastUpdated) return true;
    const ageMs = Date.now() - this.macroLastUpdated.getTime();
    return ageMs > 8 * 60 * 60 * 1000;
  }

  // ── Main loop ─────────────────────────────────────────────────────────────────

  async run(): Promise<void> {
    /** Run the agent continuously using recursive setTimeout. */
    await this.initialise();

    logInfo(`Agent running. Cycle: ${CYCLE_HOURS}h. Min SMS: ${MIN_SMS}`);
    logInfo("This agent generates intelligence alerts. It does NOT execute trades.");

    const tick = async (): Promise<void> => {
      try {
        await this.runCycle();
      } catch (e) {
        logError(`Cycle error: ${e}`);
        // Errors never stop the agent — Safety Principle 6 (graceful degradation)
      }
      setTimeout(tick, CYCLE_HOURS * 3600 * 1000);
    };

    await tick();
  }
}

// ── Entry point ───────────────────────────────────────────────────────────────

const agent = new PSGTokenAgent();
agent.run().catch((e) => logError(`Fatal: ${e}`));

// ── What to change to use this for a different token ─────────────────────────
// 1. TOKEN_SYMBOL = "BAR"  (or CITY, JUV, etc.)
// 2. SPORT = "football"    (same — all Socios football tokens)
// 3. CLUB_NAME = "FC Barcelona"
// 4. Replace getUpcomingEvents() with your fixture data source
// 5. Optionally add live lineup fetch before generateSignal()
//    See platform/realtime-integration-patterns.md Pattern 2
//
// See 04-multi-sport-agent.py for monitoring multiple tokens/sports
