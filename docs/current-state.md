# Current State

Last updated: 2026-09-16 (13-day-delay recall checks run — mechanisms stuck, names/details faded; node 4 state machines taught to explained).

## What exists

- This documentation seed (6 files) — the spine, thesis, learner model, state, decision log, handoff.
- `lessons/` + `tools/make_audio.py` — the audio-lesson modality (from earlier work). Proven to generate; **unproven to retain** (see thesis H1).
- First loop artifacts: `maps/software-development.md` (14 nodes scored: 4 known / 8 edge / 2 unknown) and `sessions/2026-08-26-software-development-probe.md`. Deep-dive plan "State, invariants, and crashes": node 1 (crash windows) `known` at `applied` (unaided, 2026-08-31; recalled unaided 2026-09-03); node 2 (transactions/atomicity) `known` at `explained` + proof-chain now demonstrated unaided (2026-09-03); node 3 (races/write-boundary enforcement) `known` at `explained`+ — guarded-write mechanism re-derivable at 13 days, rowcount/invariant/enforcement names gone at 13 days and re-presented (2026-09-16); node 4 (state machines) `known` at `explained` (taught 2026-09-16, transfer with one sharpening); node 5 (idempotency) not started — last node of the deep-dive. Node 1 fading on schedule: recognizable-only at 13 days (2026-09-16), 2nd re-presentation done. Session logs: `sessions/2026-08-31-node1-crash-windows.md`, `sessions/2026-09-01-node2-transactions.md`, `sessions/2026-09-03-node3-races-write-boundary.md`, `sessions/2026-09-16-recall-checks-node4-state-machines.md`.

## What has been tried (outside this system)

- Long-form audio lesson on the `socratic-partner` project (~50 min, `en-US-GuyNeural`). Result: useful orientation, weak retention → motivated this project.

## The next smallest milestone

Node 4 (state machines) taught 2026-09-16 to `explained`: probe showed edge ("CLOSING buys less loss", mechanism muddy); taught middle-state-as-crash-witness; lock-in passed applied-level unaided ("OPEN is too general to tell you which failure mode to run"); pizza-transfer achieved with one sharpening. Next session: teach node 5 (idempotency) — final node of the frozen deep-dive; anchor on the learner's own recalled definition ("1 run or 50 runs → same final outcome") and re-present crash-window specifics inside it. Owed recall checks ~2026-09-19 (short 3-day interval, all re-presented 2026-09-16): (1) rowcount guard (write ≠ check-the-write); (2) invariant / enforcement-at-write-boundary names; (3) keyed-receipt trick (retry checks receipt, never balance); (4) crash-window specifics (between commits; duplication-vs-loss choice). 2026-09-16 retention pattern: manipulated mechanisms stick (races, atomicity recalled/re-derivable at 13 days); names and lookup details evaporate. New standing rule in session-handoff.md: agent must check the real date and compute elapsed time whenever the learner says "it's been a while."

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
