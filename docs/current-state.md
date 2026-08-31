# Current State

Last updated: 2026-08-26 (founding session + first loop: probe complete)

## What exists

- This documentation seed (6 files) — the spine, thesis, learner model, state, decision log, handoff.
- `lessons/` + `tools/make_audio.py` — the audio-lesson modality (from earlier work). Proven to generate; **unproven to retain** (see thesis H1).
- First loop artifacts: `maps/software-development.md` (14 nodes scored: 4 known / 8 edge / 2 unknown) and `sessions/2026-08-26-software-development-probe.md`. Deep-dive plan "State, invariants, and crashes" frozen; teaching not yet started.

## What has been tried (outside this system)

- Long-form audio lesson on the `socratic-partner` project (~50 min, `en-US-GuyNeural`). Result: useful orientation, weak retention → motivated this project.

## The next smallest milestone

First loop status: **probe complete, plan frozen, teaching not started.** Next session: teach node 1 (crash windows) of the frozen deep-dive plan, one node at a time with checks; then run the owed recall check (~2026-08-29) on the five presented-only concepts — crash window, atomicity, thundering herd, least privilege, mocks-reflect-assumptions.

## Known risks / open decisions

- Folder name (`learning-library`) is provisional; rename freely — docs use relative links.
- Knowledge-tree / public-skill-graph idea is parked (thesis H4) until the private loop works.
- No knowledge representation format is chosen beyond plain markdown. When a second use case demands it (e.g., syncing to an external tool), add an **adapter**, don't migrate the core.
- Communication: Discord is the expected first channel and the learner's home for agents, but it is an adapter. Socratic-partner may later act as a questioning surface; evaluate after the private loop works, not before.
- Unprompted spaced-retrieval pings (thesis H5) are the planned retention engine — defaults off, low frequency first, learner-tolerance is itself an experiment.
- **Intake gap (open):** the thesis promises stress-testing of *whatever the learner consumed*, but there is no defined way yet for the learner to report outside intake ("I read/watched X today") so the system can probe it. Not needed for the first loop (the agent is the intake); required before the "read ten books" scenario works. This is need #1 — build on need #2.
- Voice conversation (walk-and-talk: interrupt the agent, ask, debate) is a confirmed-wanted synchronous modality — the opposite end of the spectrum from async pings. Likely future adapter: Discord voice or a speech-to-text loop over the same teaching core. Parked as need #1 until a second request.
- DHH "two weeks" claim is motivation, not evidence — the learner explicitly endorsed treating it that way. One Eero Alvar video (`ciC6ffUqI8k`) not yet reviewed.
- Real-world landscape (audited 2026-08-26, from training knowledge, not live-verified): closest existing systems are Math Academy and ALEKS (knowledge-graph mastery learning), Execute Program (retention-gated progression), Anki+FSRS (adopt FSRS for review scheduling when needed — do not invent one), Orbit/mnemonic medium (retrieval woven into intake), and 2024–2025 AI tutors (ChatGPT Study Mode, Khanmigo, LearnLM). No known system tracks the epistemic axis (knowledge rotting under the learner) — that integration appears to be this project's distinctive ground. Academic field for the mastery axis: "knowledge tracing."
