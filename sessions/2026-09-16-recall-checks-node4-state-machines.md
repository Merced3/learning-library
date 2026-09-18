# Session — Owed recall checks (13-day delay) + node 4: state machines (taught to explained)

Date: 2026-09-16
Model: moonshotai/kimi-k3 (verified via PI_MODEL at close)
Goal: Run the owed ~2026-09-06 recall checks (late by 10 days → 13-day delay since 2026-09-03), then teach node 4 (state machines) anchored on the learner's OPEN→CLOSING→COMPLETE rail.

## Context note

Learner returned after a personal break (taxes); explicitly distrusted current-state.md's freshness — correct instinct, and the recall checks re-measured instead of trusting. Learner set a new standing rule: when he says "it's been a while," the agent must get the real current date and compute elapsed time before trusting state. Recorded in docs/session-handoff.md ("Date awareness").

## Recall check results (13-day delay, harder than the planned ~3-day)

| concept | result | grade |
|---|---|---|
| guarded write as race fix | first answer wrong layer again ("fail fast / busy layer" — same mislabel as node 3, self-corrected after scaffold); rebuilt mechanism in own words once scaffolded ("they see a different beginning state") | re-derivable |
| atomicity (name + concept) | produced both unaided mid-conversation ("group 2 things, both or none — Atomicity?") | recallable, 13 days |
| rowcount guard detail | not remembered; re-presented (write ≠ check-the-write-landed); learner then generalized unprompted: "a write doesn't check anything — those are 2 different things" | gone → re-presented → re-derivable |
| invariant / enforcement-at-write-boundary | clean "no idea"; re-presented (invariant = one-step-at-a-time law; enforcement = the WHERE clause as border checkpoint); restated correctly and asked whether each transition has its own guard (yes) | gone → re-presented → re-derivable |
| keyed-usage-record trick | atomicity half solid (charge+record welded, both-or-neither); lookup target wrong (said retry checks the balance); re-presented: balance is a number that changes for many reasons — retry checks the keyed receipt (conversation, event type), never the balance | partial → re-presented |
| node-1 crash window (2nd interval) | kept scope ("interval where crash → bad things"), lost both specifics (between durable steps/commits; damage = duplication-or-loss choice) — same fade pattern as 2026-08-31 | recognizable → re-presented |

Pattern: mechanisms the learner has manipulated stick (races, atomicity); names and lookup details evaporate (invariant/enforcement names, keyed receipt, rowcount). Crash window has now faded the same way twice → weakest strand; give it a short-interval rep and fold it into node 5 (idempotency) where it naturally re-appears.

## Node 4 teaching (state machines)

1. **Probe (before teaching):** "why does CLOSING exist at all?" Learner: "buys no-loss — probably less loss" — connected to crash windows unprompted (good transfer) but mechanism muddy → edge, taught.
2. **Step 1 (the middle state):** taught plainly — completion work is slow and outside the DB; CLOSING is a visible in-progress marker buying (a) the gate (guarded write, node 3) and (b) a crash witness: state after crash tells you which damage mode you're in and what recovery is safe. Lock-in (crash after LLM, before Discord send): learner answered applied-level unaided — status CLOSING, re-run LLM (cents lost, fine), user can't tell; "OPEN is too general of a state to tell you what type of failure mode to run." Locked.
3. **Step 2 (the name + shape):** state machine = exactly one of a small list of states + allowed transitions + each transition a guarded write. Payoff: shape appears everywhere (orders, payments, CI). Lock-in 2 (pizza transfer, driver app crashes at OUT_FOR_DELIVERY): learner got "state tells you where to resume"; cost reasoning vague → sharpened: the state narrows what needs redoing (resume delivery, don't rebake = don't duplicate). Graded known (explained); transfer achieved with one sharpening.

## Evidence notes

- Learner's wrong-layer instinct ("fail fast") persists as first-answer reflex under cold recall, but self-correction now happens with one scaffold instead of a full re-teach — improving.
- Unprompted generalizations continue when material lands ("write ≠ check", "OPEN too general to pick the failure mode").
- Learner tolerates the check-then-teach rhythm well after a break; no fatigue wall hit this session (shorter session, one node).

## Owed next

- Recall checks ~2026-09-19 (short interval, 3 days): rowcount guard, invariant/enforcement names, keyed-receipt trick, crash window specifics (2nd re-presentation).
- Node 5 (idempotency) — final node of the frozen deep-dive; natural anchor: learner's own "1 run or 50 runs → same final outcome" (recalled unaided 2026-09-03) + crash-window re-appearance.
