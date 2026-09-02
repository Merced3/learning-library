# Current State

Last updated: 2026-09-03 (node-2 proof re-run passed unaided; node 3 races/write-boundary enforcement taught and locked; owed recall checks run).

## What exists

- This documentation seed (6 files) — the spine, thesis, learner model, state, decision log, handoff.
- `lessons/` + `tools/make_audio.py` — the audio-lesson modality (from earlier work). Proven to generate; **unproven to retain** (see thesis H1).
- First loop artifacts: `maps/software-development.md` (14 nodes scored: 4 known / 8 edge / 2 unknown) and `sessions/2026-08-26-software-development-probe.md`. Deep-dive plan "State, invariants, and crashes": node 1 (crash windows) `known` at `applied` (unaided, 2026-08-31; recalled unaided 2026-09-03); node 2 (transactions/atomicity) `known` at `explained` + proof-chain now demonstrated unaided (2026-09-03); node 3 (races/write-boundary enforcement) `known` at `explained`+ (transfer shown with one correction, 2026-09-03); nodes 4–5 (state machines → idempotency) not started. Session logs: `sessions/2026-08-31-node1-crash-windows.md`, `sessions/2026-09-01-node2-transactions.md`, `sessions/2026-09-03-node3-races-write-boundary.md`.

## What has been tried (outside this system)

- Long-form audio lesson on the `socratic-partner` project (~50 min, `en-US-GuyNeural`). Result: useful orientation, weak retention → motivated this project.

## The next smallest milestone

Node 3 (races / write-boundary enforcement) taught and locked on 2026-09-03, grounded in real store.py guarded writes (`WHERE status='OPEN'` + `rowcount != 1`): learner got the race mechanism unaided after a plain-language re-teach, named invariant vs enforcement with correction, and transferred the guarded-write pattern to a wallet scenario with one correction round (self-reported "still not confident" — consistent with first landing). Next session: teach node 4 (state machines) of the frozen deep-dive. Owed recall checks ~2026-09-06: (1) guarded-write as the race fix; (2) invariant vs enforcement-at-write-boundary names; (3) keyed-usage-record trick (re-derivable on 2026-09-03, not yet recallable); (4) node-1 crash window (second interval). Also owed from earlier: node-2 atomicity/rollback + charge-before-point-of-no-return had proof re-run PASSED unaided 2026-09-03; idempotency-as-result-invariant recalled unaided 2026-09-03 (~2 days after re-presentation — first evidence re-presentation → delayed recall works). Still-failed concepts from 2026-08-31 (thundering herd, least privilege, mocks-reflect-assumptions) re-present when their strands come up, then re-check with delay.

## Known risks / open decisions

- Folder name (`learning-library`) is provisional; rename freely — docs use relative links.
- Knowledge-tree / public-skill-graph idea is parked (thesis H4) until the private loop works.
- No knowledge representation format is chosen beyond plain markdown. When a second use case demands it (e.g., syncing to an external tool), add an **adapter**, don't migrate the core.
- Communication: Discord is the expected first channel and the learner's home for agents, but it is an adapter. Socratic-partner may later act as a questioning surface; evaluate after the private loop works, not before.
- Unprompted spaced-retrieval pings (thesis H5) are the planned retention engine — defaults off, low frequency first, learner-tolerance is itself an experiment.
- **Intake gap (open):** the thesis promises stress-testing of *whatever the learner consumed*, but there is no defined way yet for the learner to report outside intake ("I read/watched X today") so the system can probe it. Not needed for the first loop (the agent is the intake); required before the "read ten books" scenario works. This is need #1 — build on need #2.
- Voice conversation (walk-and-talk: interrupt the agent, ask, debate) is a confirmed-wanted synchronous modality — the opposite end of the spectrum from async pings. Likely future adapter: Discord voice or a speech-to-text loop over the same teaching core. Second in-session evidence point (2026-09-03): text ambiguity caused a describing-vs-prescribing misread; learner hypothesizes voice prosody/tone would help disambiguate and slow phrasing where needed. Still parked as need #1 until a live test is run.
- DHH "two weeks" claim is motivation, not evidence — the learner explicitly endorsed treating it that way. One Eero Alvar video (`ciC6ffUqI8k`) not yet reviewed.
- "Is markdown a professional knowledge store?" is now an open decision (2026-08-29) with live
  evidence. Answer it after the handoff test; options range from stay-on-markdown to a
  deliberate entity/schema/DB upgrade. Don't settle by default.
- Real-world landscape (audited 2026-08-26, from training knowledge, not live-verified): closest existing systems are Math Academy and ALEKS (knowledge-graph mastery learning), Execute Program (retention-gated progression), Anki+FSRS (adopt FSRS for review scheduling when needed — do not invent one), Orbit/mnemonic medium (retrieval woven into intake), and 2024–2025 AI tutors (ChatGPT Study Mode, Khanmigo, LearnLM). No known system tracks the epistemic axis (knowledge rotting under the learner) — that integration appears to be this project's distinctive ground. Academic field for the mastery axis: "knowledge tracing."
