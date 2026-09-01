# Current State

Last updated: 2026-09-01 (deep-dive node 2 taught, graded known (explained); lessons grounded against real socratic-partner code).

## What exists

- This documentation seed (6 files) — the spine, thesis, learner model, state, decision log, handoff.
- `lessons/` + `tools/make_audio.py` — the audio-lesson modality (from earlier work). Proven to generate; **unproven to retain** (see thesis H1).
- First loop artifacts: `maps/software-development.md` (14 nodes scored: 4 known / 8 edge / 2 unknown) and `sessions/2026-08-26-software-development-probe.md`. Deep-dive plan "State, invariants, and crashes": node 1 (crash windows) `known` at `applied` (unaided, 2026-08-31); node 2 (transactions/atomicity) `known` at `explained` (2026-09-01, application still mixed); nodes 3–5 (races/write-boundary → state machines → idempotency) not started. Session logs: `sessions/2026-08-31-node1-crash-windows.md`, `sessions/2026-09-01-node2-transactions.md`.

## What has been tried (outside this system)

- Long-form audio lesson on the `socratic-partner` project (~50 min, `en-US-GuyNeural`). Result: useful orientation, weak retention → motivated this project.

## The next smallest milestone

Node 2 (transactions/atomicity) is `known` at level `explained` (2026-09-01; applied re-test same day surfaced real gaps — envelope scope, skip-check, proof chain — corrected but proof question not answered unaided before fatigue; grade stays `explained`): mechanism explained in own words, boundary selection correct unaided (money writes in, Discord out), damage-mode naming per boundary correct (applied-level). Next session: quick fresh re-run of the proof question (record exists → balance was decremented, because atomicity makes record+subtraction inseparable), then teach node 3 (races / write-boundary enforcement — the learner's Q1/Q3 probe gap) of the frozen deep-dive. Owed recall checks, all ~2026-09-03: (1) node 1 crash-window concept; (2) idempotency-as-result-invariant (failed a 1-day unaided recall on 2026-09-01 — asked what it means, re-derived instantly on re-presentation); (3) node 2 atomicity/rollback + charge-before-point-of-no-return. Still-failed concepts from 2026-08-31 (thundering herd, least privilege, mocks-reflect-assumptions) re-present when their strands come up, then re-check with delay. Verified grounding (2026-09-01, repo read): socratic-partner already embodies both lessons — `with self._connection()` transaction boundaries (rollback on exception) in store.py; CLOSING + reopen_conversation is the reset/retry mechanism in _complete_conversation; `UPDATE ... WHERE status='OPEN'` guarded write in mark_conversation_closing used as the idempotency pattern example.

## Known risks / open decisions

- Folder name (`learning-library`) is provisional; rename freely — docs use relative links.
- Knowledge-tree / public-skill-graph idea is parked (thesis H4) until the private loop works.
- No knowledge representation format is chosen beyond plain markdown. When a second use case demands it (e.g., syncing to an external tool), add an **adapter**, don't migrate the core.
- Communication: Discord is the expected first channel and the learner's home for agents, but it is an adapter. Socratic-partner may later act as a questioning surface; evaluate after the private loop works, not before.
- Unprompted spaced-retrieval pings (thesis H5) are the planned retention engine — defaults off, low frequency first, learner-tolerance is itself an experiment.
- **Intake gap (open):** the thesis promises stress-testing of *whatever the learner consumed*, but there is no defined way yet for the learner to report outside intake ("I read/watched X today") so the system can probe it. Not needed for the first loop (the agent is the intake); required before the "read ten books" scenario works. This is need #1 — build on need #2.
- Voice conversation (walk-and-talk: interrupt the agent, ask, debate) is a confirmed-wanted synchronous modality — the opposite end of the spectrum from async pings. Likely future adapter: Discord voice or a speech-to-text loop over the same teaching core. Parked as need #1 until a second request.
- DHH "two weeks" claim is motivation, not evidence — the learner explicitly endorsed treating it that way. One Eero Alvar video (`ciC6ffUqI8k`) not yet reviewed.
- "Is markdown a professional knowledge store?" is now an open decision (2026-08-29) with live
  evidence. Answer it after the handoff test; options range from stay-on-markdown to a
  deliberate entity/schema/DB upgrade. Don't settle by default.
- Real-world landscape (audited 2026-08-26, from training knowledge, not live-verified): closest existing systems are Math Academy and ALEKS (knowledge-graph mastery learning), Execute Program (retention-gated progression), Anki+FSRS (adopt FSRS for review scheduling when needed — do not invent one), Orbit/mnemonic medium (retrieval woven into intake), and 2024–2025 AI tutors (ChatGPT Study Mode, Khanmigo, LearnLM). No known system tracks the epistemic axis (knowledge rotting under the learner) — that integration appears to be this project's distinctive ground. Academic field for the mastery axis: "knowledge tracing."
