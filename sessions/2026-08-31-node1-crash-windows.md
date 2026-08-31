# Session — Deep-dive node 1: crash windows (taught to applied)

Date: 2026-08-31
Model: moonshotai/kimi-k3 (verified via PI_MODEL at close)
Goal: Teach node 1 (crash windows) of the frozen "State, invariants, and crashes" deep-dive; run the overdue 2026-08-29 recall check first (learner chose full-check-then-teach).

## What happened

1. Ran delayed recall check (~5 days) on the five presented-only concepts from 2026-08-26 scoring feedback. Result: **0/5 recalled unaided.** Crash window: partial shape retained (scope: "ways the program can crash") but the time-gap mechanism replaced with "ways we solve crashes." Atomicity, least privilege, mocks-reflect-assumptions: gone. Thundering herd: confused with fail-fast (fail-fast vs queueing strand). Levels per AGENTS.md: all presented-only → now `edge`; recall-check structure validated as a targeting instrument.
2. Taught node 1 (crash windows), anchored to socratic-partner's `/done` flow: definition = time interval where a crash does damage; game = shrink window toward one operation.
3. Lock-in 1: learner correctly rejected "before DB write," walked through write/process/send, and located the real window at the **message-send** step — duplication-vs-loss trade-off ("do we try again? repeat message, we don't want that"). Also self-corrected mid-answer ("wait what am I answering") and generalized: multiple crash windows exist, boundary-shaped.
4. Lock-in 2: why naive resume-and-retry fails — unaided, correct (unknown delivery → duplication/loss). `applied` level demonstrated.
5. Learner spontaneously extended to idempotency as **result invariant** ("same ending result every time, no matter where it crashed" — exactly-once semantics) and inferred node 2's role (crash can't split an atomic write). Flagged as node 5/node 2 territory; teacher stopped per one-step discipline.
6. Session closed; owed recall check on node-1 concepts set for ~2026-09-03.

## Evidence notes

- All answers unaided; teacher withheld feedback during the 5-concept recall check so later answers weren't coached. Learner-meta comment: "repetitions, which is what this is" — correctly identified the spaced-retrieval loop. Engagement positive.
- First retention measurement of the system: supports thesis H1 (presentation alone doesn't retain) at n=1. Logged in decision log as evidence, not verdict.

## Next session

Teach node 2 (transactions/atomicity) — anchor on the learner's own spontaneous inference that "the crash can't split the write." Then nodes 3–5 of the frozen plan. Node-1 recall check owed ~2026-09-03; the four failed concepts re-present inside their future nodes and re-checked with delay.
