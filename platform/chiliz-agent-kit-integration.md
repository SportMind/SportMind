# Chiliz Agent Kit Integration

**How to connect SportMind's intelligence layer to the Chiliz Agent Kit
execution layer — the complete pipeline from natural language intent to
on-chain fan token action.**

The Chiliz Agent Kit (TypeScript SDK) allows agents to transfer CHZ, trade
fan tokens, and interact with Chiliz smart contracts via LangChain. SportMind
provides the intelligence that determines *whether* and *when* to act.
Together they form a complete sports intelligence + execution stack.

---

## The intelligence-execution pipeline

```
PIPELINE OVERVIEW:

Natural Language Input:
  "Buy 10 PSG tokens if they win tonight"
  "Add $100 of BAR to the pool before El Clásico if signal is strong"
  "Vote YES on the stadium naming governance proposal"

SportMind Layer (intelligence — this library):
  1. Check macro state (is the crypto market in a state where token action is sensible?)
  2. Load fan token signal for $PSG/$BAR
  3. Check upcoming event signal (has PSG won? is El Clásico imminent?)
  4. Assess governance signal (what does the LTUI model say about YES vs NO?)
  5. Output: recommended_action + confidence + flags + reasoning

Application Decision Layer (your code):
  6. Parse recommended_action from SportMind output
  7. Check if action conditions are met
  8. Request human approval if autonomy level requires it (Level 0-1)
  9. Pass approved action to Chiliz Agent Kit

Chiliz Agent Kit Layer (execution — not SportMind):
  10. Execute the approved transaction on Chiliz Chain
  11. Confirm transaction
  12. Report outcome back to your application

KEY PRINCIPLE: Steps 1-5 are SportMind. Steps 6-9 are your code.
Steps 10-12 are Chiliz Agent Kit. SportMind never touches steps 10-12.
```

---

## Setup

```bash
# Install dependencies
npm install chiliz-agent-kit @langchain/core langchain

# Python side (SportMind intelligence)
pip install aiohttp anthropic mcp
```

```typescript
// Environment variables
SPORTMIND_API=http://localhost:8080      // Local SportMind Skills API
ANTHROPIC_API_KEY=your_key_here          // For Claude reasoning
CHILIZ_PRIVATE_KEY=your_wallet_key       // For Chiliz Agent Kit transactions
CHILIZ_RPC_URL=https://rpc.chiliz.com    // Chiliz Chain RPC
```

---

## Pattern 1 — Natural language intent to token action

```typescript
// sportmind-chiliz-agent.ts
/**
 * Complete pipeline: Natural language → SportMind intelligence → Chiliz execution
 *
 * The intelligence layer (SportMind) runs first.
 * The execution layer (Chiliz Agent Kit) runs only if intelligence approves.
 */
import { createChilizAgentKit } from 'chiliz-agent-kit';
import Anthropic from '@anthropic-ai/sdk';

const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
const chilizKit  = createChilizAgentKit({
  privateKey: process.env.CHILIZ_PRIVATE_KEY!,
  rpcUrl:     process.env.CHILIZ_RPC_URL!,
});

interface SportMindSignal {
  token:            string;
  recommended_action: 'ENTER' | 'WAIT' | 'REDUCE' | 'ABSTAIN';
  sms:              number;
  macro_modifier:   number;
  flags:            Record<string, boolean>;
  reasoning:        string;
}

// ── Step 1: Get SportMind intelligence ───────────────────────────────────────
async function getSportMindSignal(
  sport: string,
  token: string,
  eventContext?: string
): Promise<SportMindSignal> {
  /**
   * Use Claude with SportMind MCP tools to generate intelligence signal.
   * This is the intelligence layer — no execution happens here.
   */
  const response = await anthropic.beta.messages.create({
    model:      'claude-sonnet-4-20250514',
    max_tokens: 1500,
    system: `You are a SportMind intelligence agent. You have access to SportMind
    MCP tools. For any sports analysis:
    1. ALWAYS call sportmind_macro FIRST
    2. Call sportmind_signal for the specific token/event
    3. Output ONLY a JSON object with this structure:
    {
      "token": string,
      "recommended_action": "ENTER" | "WAIT" | "REDUCE" | "ABSTAIN",
      "sms": number (0-100),
      "macro_modifier": number,
      "flags": object,
      "reasoning": string (one sentence)
    }
    Never recommend direct execution. Your role is intelligence only.`,
    mcp_servers: [{
      type: 'url' as const,
      url:  `${process.env.SPORTMIND_API}/mcp`,
      name: 'sportmind'
    }],
    messages: [{
      role:    'user',
      content: `Generate signal for ${token} token. Sport: ${sport}. ${eventContext || ''}`
    }]
  });

  // Extract JSON from response
  const text = response.content
    .filter(b => b.type === 'text')
    .map(b => (b as {type: 'text', text: string}).text)
    .join('');

  const jsonMatch = text.match(/\{[\s\S]*\}/);
  if (!jsonMatch) throw new Error('SportMind did not return valid JSON signal');

  return JSON.parse(jsonMatch[0]) as SportMindSignal;
}

// ── Step 2: Parse natural language intent ────────────────────────────────────
interface ParsedIntent {
  action:     'BUY' | 'SELL' | 'VOTE' | 'STAKE' | 'CHECK';
  token:      string;
  amount?:    number;
  currency?:  string;
  condition?: string;
  voteChoice?: 'YES' | 'NO';
}

function parseIntent(naturalLanguage: string): ParsedIntent {
  /**
   * Simple intent parser — in production use a dedicated NLP model or
   * Claude's function calling to extract structured intent from natural language.
   */
  const lower = naturalLanguage.toLowerCase();
  const tokenMatch = lower.match(/\$([a-z]+)/i) || lower.match(/(psg|bar|city|juve|rmfc)/i);
  const amountMatch = lower.match(/(\d+(?:\.\d+)?)\s*(?:tokens?|chz|\$)/i);

  return {
    action:   lower.includes('buy') ? 'BUY' :
              lower.includes('sell') ? 'SELL' :
              lower.includes('vote') ? 'VOTE' :
              lower.includes('stake') ? 'STAKE' : 'CHECK',
    token:    tokenMatch ? tokenMatch[1].toUpperCase() : '',
    amount:   amountMatch ? parseFloat(amountMatch[1]) : undefined,
    condition: lower.includes('if they win') ? 'IF_WIN' :
               lower.includes('if signal') ? 'IF_SIGNAL_STRONG' : undefined,
  };
}

// ── Step 3: Decision gateway (the safety layer) ──────────────────────────────
interface GatewayDecision {
  approved:    boolean;
  reason:      string;
  requiresHuman: boolean;
}

function evaluateGateway(
  intent:    ParsedIntent,
  signal:    SportMindSignal,
  autonomyLevel: 0 | 1 | 2 | 3 | 4
): GatewayDecision {
  /**
   * THE CRITICAL SAFETY LAYER.
   * SportMind intelligence + user intent → should we execute?
   *
   * This function implements Safety Principle 1 from core/autonomous-agent-framework.md:
   * Intelligence separation — the agent generates intelligence; the application decides.
   */

  // Hard blocks (safety principles from autonomous-agent-framework.md)
  if (signal.flags['macro_override_active']) {
    return { approved: false, reason: 'Macro override active — market conditions unfavourable', requiresHuman: true };
  }
  if (signal.flags['liquidity_critical']) {
    return { approved: false, reason: 'Liquidity critical — insufficient pool depth', requiresHuman: true };
  }
  if (signal.sms < 60) {
    return { approved: false, reason: `Signal quality too low (SMS ${signal.sms}) — insufficient confidence`, requiresHuman: true };
  }

  // Financial actions: always require human at Level 0-1
  if (['BUY', 'SELL', 'STAKE'].includes(intent.action) && autonomyLevel <= 1) {
    return {
      approved: false,
      reason: `Level ${autonomyLevel} autonomy: financial actions require human approval`,
      requiresHuman: true
    };
  }

  // Check conditions
  if (intent.condition === 'IF_WIN' && signal.recommended_action !== 'ENTER') {
    return { approved: false, reason: `Condition not met: signal is ${signal.recommended_action}`, requiresHuman: false };
  }
  if (intent.condition === 'IF_SIGNAL_STRONG' && signal.sms < 80) {
    return { approved: false, reason: `Signal not strong enough (SMS ${signal.sms} < 80)`, requiresHuman: false };
  }

  // Approved
  return { approved: true, reason: `Signal strong (SMS ${signal.sms}), conditions met`, requiresHuman: false };
}

// ── Step 4: Execute via Chiliz Agent Kit (only if approved) ──────────────────
async function executeAction(intent: ParsedIntent, signal: SportMindSignal): Promise<string> {
  /**
   * Execution layer — Chiliz Agent Kit handles the actual blockchain interaction.
   * This function is ONLY called after gateway approval.
   */
  console.log(`Executing: ${intent.action} ${intent.amount || ''} $${intent.token}`);
  console.log(`SportMind reasoning: ${signal.reasoning}`);

  switch (intent.action) {
    case 'BUY':
      // Chiliz Agent Kit: buy fan tokens
      // const result = await chilizKit.buyFanToken({
      //   symbol: intent.token,
      //   amount: intent.amount!,
      //   slippage: 0.5  // 0.5% max slippage
      // });
      return `Would execute: BUY ${intent.amount} $${intent.token} via Chiliz Agent Kit`;

    case 'VOTE':
      // Chiliz Agent Kit: submit governance vote
      // const result = await chilizKit.submitGovernanceVote({
      //   token: intent.token,
      //   proposalId: ...,
      //   choice: intent.voteChoice
      // });
      return `Would execute: VOTE ${intent.voteChoice} on $${intent.token} governance`;

    default:
      return `Action ${intent.action} not yet implemented`;
  }
}

// ── Main: the complete pipeline ───────────────────────────────────────────────
async function processFanTokenIntent(
  naturalLanguage: string,
  sport:           string,
  autonomyLevel:   0 | 1 | 2 | 3 | 4 = 1  // Default: advisory (human approves)
): Promise<void> {
  console.log(`\nInput: "${naturalLanguage}"`);
  console.log('─'.repeat(50));

  // Step 1: Parse intent
  const intent = parseIntent(naturalLanguage);
  console.log(`Intent: ${intent.action} $${intent.token} ${intent.condition || ''}`);

  // Step 2: Get SportMind intelligence
  console.log('Getting SportMind signal...');
  const signal = await getSportMindSignal(sport, intent.token, naturalLanguage);
  console.log(`Signal: ${signal.recommended_action} | SMS: ${signal.sms} | Macro: ${signal.macro_modifier}`);
  console.log(`Reasoning: ${signal.reasoning}`);

  // Step 3: Gateway decision
  const decision = evaluateGateway(intent, signal, autonomyLevel);
  console.log(`Gateway: ${decision.approved ? '✅ APPROVED' : '❌ BLOCKED'} — ${decision.reason}`);

  if (!decision.approved) {
    if (decision.requiresHuman) {
      console.log('→ Escalating to human review');
      // Send to human review channel here
    }
    return;
  }

  // Step 4: Execute (only reaches here if gateway approved)
  const result = await executeAction(intent, signal);
  console.log(`Execution: ${result}`);
}

// Example usage
processFanTokenIntent(
  "Buy 10 PSG tokens if the signal is strong",
  "football",
  1  // Level 1: advisory — would need human approval for actual execution
);
```

---

## Pattern 2 — Automated pre-match action trigger

```typescript
// pre_match_trigger.ts
/**
 * Pattern 2: Schedule-based trigger that automatically evaluates and
 * (with appropriate autonomy level) executes pre-match fan token actions.
 */
import { EventEmitter } from 'events';

interface ScheduledAction {
  token:         string;
  sport:         string;
  event_id:      string;
  intended_action: 'BUY' | 'INCREASE_POSITION';
  amount:        number;
  trigger_at:    'T-48h' | 'T-2h' | 'T-0';
  min_sms:       number;  // Minimum SMS to proceed
  autonomy_level: 0 | 1 | 2;
}

class PreMatchActionScheduler extends EventEmitter {
  private scheduled: ScheduledAction[] = [];

  schedule(action: ScheduledAction) {
    this.scheduled.push(action);
    console.log(`Scheduled: ${action.intended_action} $${action.token} at ${action.trigger_at} before ${action.event_id}`);
  }

  async evaluate(action: ScheduledAction): Promise<void> {
    // Get current SportMind signal
    const signal = await getSportMindSignal(action.sport, action.token);

    // Check trigger conditions
    if (signal.sms < action.min_sms) {
      console.log(`[${action.event_id}] SMS ${signal.sms} < min ${action.min_sms} — skipping`);
      return;
    }

    if (signal.recommended_action !== 'ENTER') {
      console.log(`[${action.event_id}] Signal is ${signal.recommended_action} — not ENTER — skipping`);
      return;
    }

    // Autonomy gate
    if (action.autonomy_level <= 1) {
      // Emit for human review
      this.emit('requires_human_approval', { action, signal });
      return;
    }

    // Level 2+: execute if approved
    await executeAction(
      { action: action.intended_action, token: action.token, amount: action.amount },
      signal
    );
  }
}

// Usage
const scheduler = new PreMatchActionScheduler();

scheduler.on('requires_human_approval', ({ action, signal }) => {
  console.log(`\n🔔 HUMAN APPROVAL REQUIRED`);
  console.log(`Token: $${action.token} | SMS: ${signal.sms}`);
  console.log(`Reasoning: ${signal.reasoning}`);
  console.log(`Action: ${action.intended_action} ${action.amount}`);
  // → Send to your approval workflow (Slack, email, push notification)
});

scheduler.schedule({
  token: 'PSG', sport: 'football',
  event_id: 'ucl-qf-psg-arsenal',
  intended_action: 'BUY', amount: 50,
  trigger_at: 'T-2h', min_sms: 75,
  autonomy_level: 1  // Always requires human for this token
});
```

---

## Pattern 3 — Governance vote intelligence

```typescript
// governance_intent.ts
/**
 * Pattern 3: Governance vote intelligence.
 * SportMind analyses the governance context; human decides the vote.
 * Never submits a vote autonomously — governance is always Level 0-1.
 */
async function analyseGovernanceVote(
  token:      string,
  proposalId: string,
  proposalText: string
): Promise<void> {
  const response = await anthropic.beta.messages.create({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 1500,
    system: `You are a SportMind governance intelligence agent.
    Load the governance intelligence skill and analyse the governance vote.
    Output a governance brief with:
    - Decision weight classification (Cosmetic/Operational/Commercial/Structural)
    - GSI assessment (if available)
    - LTUI_YES vs LTUI_NO projection
    - Recommendation: VOTE_YES / VOTE_NO / ABSTAIN with reasoning
    
    Important: You provide intelligence. The token holder decides.
    Never express certainty — express calibrated analysis.`,
    mcp_servers: [{ type: 'url' as const, url: `${process.env.SPORTMIND_API}/mcp`, name: 'sportmind' }],
    messages: [{
      role: 'user',
      content: `Analyse governance vote for $${token}. Proposal: "${proposalText}". Proposal ID: ${proposalId}`
    }]
  });

  const brief = response.content.filter(b => b.type === 'text').map(b => (b as any).text).join('');
  console.log('\n── Governance Intelligence Brief ──────────────────');
  console.log(brief);
  console.log('\nNOTE: This is intelligence context. The vote decision is yours.');
  console.log('SportMind never submits governance votes autonomously.');
}
```

---

## Connecting to SportFi Kit

```typescript
// The complete stack: SportMind + Chiliz Agent Kit + SportFi Kit
//
// SportMind:        intelligence layer (this library)
// Chiliz Agent Kit: blockchain execution layer
// SportFi Kit:      UI + wallet + user experience layer
//
// INTEGRATION PATTERN:
//
// User interacts with SportFi Kit UI
//   → UI calls SportMind for intelligence context
//   → SportMind returns signal (recommended_action, SMS, reasoning)
//   → UI displays intelligence to user
//   → User approves action
//   → UI calls Chiliz Agent Kit to execute
//   → Chiliz Agent Kit handles the transaction
//
// See: examples/starter-pack/05-sportfi-kit-integration.py
// See: examples/applications/app-07-sportfi-kit-integration.md

const STACK_SUMMARY = `
LAYER       TOOL                PURPOSE
────────    ──────────────────  ─────────────────────────────────────
UI/UX       SportFi Kit         Components, wallet detection, token-gating
Intelligence SportMind          Pre-match signals, fan token analysis
Execution   Chiliz Agent Kit    CHZ transfer, token trading, governance
Blockchain  Chiliz Chain        The ledger where everything happens
`;

console.log(STACK_SUMMARY);
```

---

## Security considerations

```
CRITICAL: Private key management

Never include CHILIZ_PRIVATE_KEY in SportMind skill files, prompts,
or context sent to LLMs. The private key belongs ONLY in:
  - Environment variables (server-side)
  - Secure key management (AWS KMS, Vault)
  - Never in the SportMind context window

SportMind intelligence does not need to know your private key.
It generates recommended_action. Your execution layer uses the key.
This separation is both an architectural principle and a security requirement.

See: SECURITY.md Threat 6 (prompt theft) and Threat 7 (meta-injection)
for additional security guidance relevant to agent deployments.
```

---

## Compatibility

**Agent framework:** `core/autonomous-agent-framework.md` — autonomy levels and safety principles
**Skill bundles:** `platform/skill-bundles.md` — correct bundle for fan token use cases
**SportFi Kit:** `examples/applications/app-07-sportfi-kit-integration.md` — full UI stack
**Governance:** `fan-token/sports-governance-intelligence/` — governance intelligence
**Integration partners:** `platform/integration-partners.md` — Partner 7 (SportFi Kit)

*MIT License · SportMind · sportmind.dev*
*Chiliz Agent Kit: github.com/chiliz-chain/chiliz-agent-kit*
