# Session — Deep-dive node 2: transactions/atomicity (taught to explained)

Date: 2026-09-01
Model: moonshotai/kimi-k3 (verified via PI_MODEL at close)
Goal: Teach node 2 (transactions/atomicity) of the frozen "State, invariants, and crashes" deep-dive, anchored on the learner's own 2026-08-31 inference ("crash can't split the write").

## What happened

1. Probe (unaided, ~1 day after node 1): crash between CLOSING-write and billing-write. Learner correctly predicted duplication-or-loss on re-run; guessed a transaction means "one operation → smaller crash window." Right direction, wrong mechanism.
2. Taught the correction: a transaction doesn't shrink the crash window — it makes the window unable to split the pair. Rollback discards BOTH writes; the pair becomes one indivisible unit; only two outcomes exist (both commit / neither). Named: transaction, atomicity, invariant, rollback.
3. Lock-in 1 (what does the DB show after crash mid-transaction): answered (c) neither — correct but self-flagged as a protective guess; then explained the mechanism in own words ("unit," "harmless not smaller," "only two outcomes"). Recorded as correct-with-guess, not clean unaided.
4. **Idempotency failed 1-day unaided recall**: learner asked "what does idempotency mean again?" then re-derived instantly on re-presentation. Logged as evidence for H1/H5 (n=2 against self-generation-alone retaining). Re-stated the pair: atomicity makes the crash harmless; idempotency makes the retry harmless.
5. Lock-in 2 (credit-charge design): boundary correct unaided (both money writes inside, Discord outside); placement before/after COMPLETE unresolved — clean "I really don't know." Taught: durable, recoverable-by-retry damage goes first; point-of-no-return state goes last; keyed usage record makes retry idempotent. Connected to node 1's message-send lesson.
6. Final check (order COMPLETE / archive / Discord-post, per-gap damage modes): partial. Mislabeled the archive gap as unrecoverable ("message lost forever") — actually retry-safe, archiving is a copy step. Correctly flagged the archive→Discord gap as unknown-delivery/duplication-risk (recognized node 1 from a new angle).
7. Learner self-reported a reasoning bias: treats "gap has bad outcome" as "wrong answer" — tries to fix everything. Reframed: every gap has a damage mode; design = choosing recoverable damage.
8. Learner requested grounding against the real repo ("telephone game" concern). Verified: store.py write methods use `with self._connection()` transaction boundaries (commit on success / rollback on exception); application.py `_complete_conversation` order = mark CLOSING → LLM call → send Discord message → final DB write, with `reopen_conversation` resetting CLOSING→OPEN on any failure. CLOSING+reopen IS the reset/retry mechanism from node 1/2 — the learner already built the pattern.

## Evidence notes

- Node 2 graded `known (explained)`: mechanism explained unaided, boundary selection unaided; application mixed (one of two final-check verdicts wrong). Not claimed at `applied`. Owed re-check ~2026-09-03 with delay.
- Owed recall checks ~2026-09-03: node 1 crash window; idempotency-as-result-invariant; node 2 atomicity/rollback + charge-before-point-of-no-return.
- Learner volunteered guess-flags and "I don't know" signals throughout — probe-signal quality remains high.

## Applied re-test (same session, learner-initiated)

Learner chose to push node 2 toward `applied` before moving on. Closed-book design exercise: order CLOSING / LLM call / charge / Discord / COMPLETE, name each gap's damage mode, scope the charge transaction, walk a crash-after-charge retry.

- Damage-mode naming per boundary: **correct across all four gaps** (applied-level), including honest best-case/less-optimal split on the Discord gap and the free-usage cost of the LLM→charge gap.
- Envelope scope: **wrong** — put CLOSING + LLM call inside the charge transaction. Corrected: rollback only reaches the DB; outside-world actions (LLM call, Discord send) can never live in a transaction; each DB step is its own envelope; a single write needs no wrapper (all-or-nothing on one row is automatic). Learner's alternating inside/outside picture was actually right; confusion was thinking "inside" meant one shared room.
- Retry walk: **double-charged** — missed the keyed skip-check despite it being taught 20 minutes earlier. Corrected with the guarded-write pattern from the real repo (`UPDATE ... WHERE status='OPEN'`, zero rows changed → error).
- Proof question (record exists → what does it prove about the balance, and which mechanism makes the proof trustworthy): **not answered unaided**. Learner hit a fatigue wall ("Im pretty spent", "my thinking has stopped") mid-chain. One boxed diagram of the full 5-step flow + the envelope picture landed where text hadn't. Session stopped at the wall by design.

Grade stays `known (explained)`. Owed fresh: the proof re-run (expected fast when rested — a retention data point, not a re-teach), then node 3.

## Next session

Teach node 3 (races / write-boundary enforcement — the learner's Q1/Q3 probe gap: durability answers where race-enforcement was asked). Consider grounding node 3 in the real store.py (e.g., `WHERE status = 'OPEN'` guarded updates) since repo-anchoring proved high-trust today.
