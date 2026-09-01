# Map — Software Development (coarse competency map)

Updated: 2026-08-26
Goal: Locate the learner's known/edge/unknown across the major strands of software
development, anchored to projects he built (socratic-partner, this learning system).

Method note: questions are anchored to the learner's own code where possible (thesis H8).
Status: `known` | `edge` | `unknown` | `blocked`. Evidence levels per AGENTS.md.

## Strands

| strand | status | evidence |
|---|---|---|
| Data & state — state machines (why CLOSING exists) / crash windows | known (applied) | 2026-08-31: named time-gap mechanism, located window at send step, explained why retry fails — all unaided |
| Data & state — transactions / atomicity | known (explained) | 2026-09-01: explained all-or-nothing/rollback + "unit, harmless not smaller" framing after lock-in (initial answer correct but self-flagged as guess); boundary selection correct unaided (money writes in, Discord out); placement before/after point-of-no-return needed coaching; final ordering check mixed → explained, applied not yet clean |
| Data & state — constraints at the DB boundary (races, enforcement at write) | edge | Q1/Q3: gave durability answer (true, wrong layer); missed race-condition enforcement |
| Failure & reliability — transient vs permanent failure classification | known | R2-Q3: derived retry-only-what-time-can-fix policy unaided |
| Failure & reliability — unknown process state after timeout, reset-to-known-state | edge | R2-Q1: grasped session-integrity risk, missed protocol desync/unknown-state reasoning |
| Failure & reliability — backoff, thundering herd, tight-loop costs | edge | R2-Q2 "I don't know"; 2026-08-31 recall: confused with fail-fast → edge |
| Failure & reliability — idempotency, delivery semantics, supervision | edge | 2026-09-01: idempotency re-presented inside node 2 after failed 1-day unaided recall (learner asked what it means, then re-derived instantly); delivery semantics surfaced in ordering check (duplication-vs-loss at Discord send, recognized via node 1) |
| Interfaces & boundaries — decoupling via protocol/ports | known | R3-Q2: named decoupling + swap-channel benefit unaided |
| Interfaces & boundaries — layer separation (policy vs mechanism) | edge | R3-Q1: answered active-conversation rule instead of reusability/coupling concern |
| Correctness & testing — what tests buy (regression detection not proof; AI-output authorization) | edge | R4-Q1: original AI-authorization frame (valuable), muddy on regression-vs-correctness |
| Correctness & testing — mock theater / assumption reflection | edge | R4-Q2 "infrastructure theater" instinct; 2026-08-31 recall: could not recall mechanism → edge |
| Correctness & testing — fake the nondeterministic, keep real semantics | edge | R4-Q3: data-isolation axis correct (temp real SQLite ≠ live DB); determinism-vs-semantics axis unaddressed |
| Scale & performance — fail-fast vs queueing, UX of waiting | edge | R3-Q3: complexity-avoidance answer, missed invisible-hang UX concern |
| Scale & performance — queues, backpressure, concurrency models | unprobed | |
| Security — least privilege / blast radius | edge | R5-Q1 insurance analogy correct shape; 2026-08-31 recall: could not recall re-presented principle → edge |
| Process — git, failed-experiment preservation | known | R5-Q2: stable main + don't-repeat-the-lesson, unaided |
| Data modeling & schema evolution — old-shape migration fixtures | known | R5-Q3: deployed data IS the contract, unaided |
| Process — rollout/rollback, review discipline | unprobed | (strong prior: lived the scheduler rollback) |
| Reading & auditing code (the "direct and review AI output" skill) | unprobed | |

## Probe log

- R1-Q1 [state machines] — partial recovery intuition, missed crash window → edge
- R1-Q2 [transactions] — "I do not know" → unknown
- R1-Q3 [DB constraint vs code check] — durability answer, missed race enforcement → edge
- R2-Q1 [timeout/reset] — session-duplication intuition, missed unknown-process-state → edge
- R2-Q2 [backoff] — "I don't know" → unknown
- R2-Q3 [billing vs rate-limit] — transient/permanent classification derived unaided → known
- R3-Q1 [scheduler/content split] — answered eligibility instead of coupling/reuse → edge
- R3-Q2 [protocol decoupling] — swap-channel benefit, correct unaided → known
- R3-Q3 [fail-fast] — complexity answer, missed UX-of-wait → edge
- R4-Q1 [purpose of tests] — AI-authorization frame + "good enough" → edge
- R4-Q2 [mock lie] — theater instinct, vague mechanism → edge
- R4-Q3 [fake clocks/real SQLite] — proximity instinct, faked/kept parts inverted → edge
- R5-Q1 [least privilege] — insurance/bounded-cost intuition, unnamed principle → edge
- R5-Q2 [preserve failed experiments] — stability + lesson-preservation, correct → known
- R5-Q3 [migration fixtures] — deployed-data-is-the-contract, correct → known
- REGRADE R4-Q3 — learner clarified "fake" meant temp-instance-not-live-DB (correct); strand row updated, status stays edge (determinism axis still unaddressed)
- 2026-08-31 RECALL CHECK (5 presented-only concepts, ~5 day delay): 0/5 recalled unaided; crash window partial-shape only; atomicity / least privilege / mocks-assumptions gone; thundering herd confused with fail-fast. All five re-presented → edge nodes; see sessions/2026-08-31-node1-crash-windows.md
- 2026-09-01 NODE 2 (transactions/atomicity) taught; see sessions/2026-09-01-node2-transactions.md. Lock-in 1 (rollback shows neither write) correct but guess-flagged, mechanism then explained unaided; credits design: boundary correct, placement before/after unresolved ("I really don't know") → taught charge-before-point-of-no-return + keyed retry; ordering check: archive gap mislabeled unrecoverable (it is retry-safe), Discord-send gap correctly flagged unknown-delivery. Idempotency failed 1-day unaided recall. Repo-verified: real socratic-partner code already uses transaction boundaries + CLOSING/reopen reset + guarded writes (`WHERE status='OPEN'`). Same-day applied re-test: damage modes per boundary correct (applied-level), envelope scope wrong, retry walk double-charged; proof chain not unaided before fatigue → grade stays `explained`; fresh proof re-run owed next session.

## Notes

- Learner flags uncertainty himself reliably ("I do not truly know") — high-quality probe
  signal; do not over-question to extract admissions he volunteers.
- Learner assumes questions are scoped to the current project unless told otherwise —
  signpost scope explicitly ("thinking beyond this project...") when a question goes general.
- **File convention**: paragraphs stored as single unwrapped lines make exact-match scripted
  edits robust; wrapping is nicer for human eyes. Either is fine for AI context-reading.
  New files should default to unwrapped paragraphs (as current-state.md already does);
  existing wrapped files stay until deliberately rewritten. Record the choice once here.
- Teacher error log: R3 map edit accidentally dropped the Correctness & testing row
  (overbroad replacement); caught and restored at R4. Verify table integrity after edits.
  A second recurring error: guessing wrapped-paragraph text when the file stores one line
  per paragraph — prefer `read`/`grep` before scripted edits on non-code files.
