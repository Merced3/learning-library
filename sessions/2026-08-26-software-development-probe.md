# Session — Software Development, probe + plan (first manual loop)

Date: 2026-08-26
Model: mixed (Claude for audit round; moonshotai/kimi-k3 otherwise) — update at session close
Goal: First manual teaching loop — validate the loop, produce first learner evidence, and map the learner across software-development strands.

## What happened

1. Learner chose goal: "software development competence" (direct/audit AI code, systems thinking over syntax memorization).
2. Ran 5 probe rounds (14 nodes scored) anchored to socratic-partner. Artifact: `maps/software-development.md`.
3. Finding: learner consistently answers "one layer up" — grasps what mechanisms do, not why they live at that layer. Root gap: invariants and enforcement boundaries.
4. Deep-dive plan frozen (approved implicitly via question, then session close chosen):
   "State, invariants, and crashes" through socratic-partner's /done flow — 5 nodes:
   crash windows → transactions → races/write-boundary → state machines → idempotency.
5. Session closed by learner choice before node 1, to test the handoff docs.

## Evidence collected (per AGENTS.md levels)

- Probe answers were unaided unless noted in the map's raw log.
- Scoring feedback contained mini-explanations (presented-only): crash window, atomicity, thundering herd, least privilege, mocks-reflect-assumptions. These are owed a delayed recall check on ~2026-08-29 — first retention test of the system. Ask the learner to explain each unaided; failures become `edge` nodes in the deep dive.

## Learner findings this session

- Volunteers uncertainty honestly — do not over-extract.
- Needs scope signposted when questions go general.
- Lost the goal mid-long-session → future sessions should re-anchor the goal periodically.
- Confirmed wants: voice modality (sync), stress-testing, async pings; consistency over optimality (H7); project-anchored teaching (H8).

## Next session

Use `docs/session-handoff.md`. Next milestone: teach node 1 (crash windows) of the frozen deep-dive plan in `maps/software-development.md`. Owed recall check: the five presented-only concepts above.
