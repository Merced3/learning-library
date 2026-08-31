# Decision Log

Append-only. Newest at the bottom. Never edit old entries except to append `OUTCOME:`. An entry is an experiment: hypothesis → intervention → evidence → verdict.

Format:

```text
## <date> — <short name>
Hypothesis: <what we believed>
Intervention: <what we did>
Evidence: <what we observed; mark unverified claims>
Verdict: keep | change | revert | inconclusive
```

---

## 2026-08-26 — Founding structure

Hypothesis: A small, explicitly-mutable documentation seed (spine + thesis + learner model + state + log + handoff) preserves direction across sessions better than a large, rigid documentation system for a project whose methods are expected to churn.

Intervention: Created 6-file seed; parked all machinery (schedulers, databases, knowledge trees) behind the "second real need" rule.

Evidence: Prior session showed a mature project (socratic-partner) where thesis-first docs prevented drift; learner rejected that full structure as too heavy for this stage.

Verdict: keep until the first teaching loop produces counter-evidence.

---

## 2026-08-26 — Audio retained as a modality, demoted as a method

Hypothesis: Long-form audio lessons orient (vocabulary, mental map) but do not retain.

Intervention: Kept `tools/make_audio.py` and `lessons/`; thesis H1 requires any future audio lesson to pair with at least one retrieval check before retention is claimed.

Evidence: Learner's self-report. No delayed-recall measurement exists yet.

Verdict: inconclusive → first teaching loop must include a delayed recall check.

---

## 2026-08-26 — Session audit (model switch: Kimi → Claude)

Hypothesis: The founding seed survives a fresh-eyes audit by a different model without
structural change.

Intervention: Full re-read of all six docs. Fixed: stray `*` in thesis H6; evidence ladder
corrected (delay is a dimension, not a top rung); added Bloom 2-sigma anchor to H2 (marked
not-live-verified); added autonomous-spend budget rule to AGENTS; named the intake-reporting
gap in current-state; recorded real-world landscape (Math Academy, ALEKS, Execute Program,
Anki/FSRS, Orbit, 2024–25 AI tutors) and the apparent niche: no known system tracks the
epistemic axis.

Evidence: Cross-model doc review; landscape from training knowledge (web search tool had no
credentials — flagged inside the notes themselves).

Verdict: keep — structure held; only content-level corrections were needed. First teaching
loop remains the next milestone.

---

## 2026-08-26 — First manual loop: probe phase complete

Hypothesis: A manual probe → map → plan loop produces usable competency evidence and valid
teaching targets without any new software.

Intervention: Ran 5 probe rounds (14 nodes) anchored to socratic-partner; wrote
maps/software-development.md; froze the "State, invariants, and crashes" deep-dive plan;
learner chose to close the session before teaching node 1 to test the handoff docs.

Evidence: 4 known / 8 edge / 2 unknown. Pattern finding: learner answers "one layer up" —
grasps what mechanisms do, not why they live at that layer (root gap: invariants and
enforcement boundaries). Learner lost the session goal mid-probe → recorded in learner.md;
future sessions should re-anchor periodically. Teacher made one map-editing error (dropped a
table row) — caught, restored, logged in map notes.

Verdict: inconclusive until node 1 is taught and the ~2026-08-29 recall check runs. The
handoff test (can a fresh session resume from docs alone?) is the next gate.

---

## 2026-08-29 — Session closeout: conventions, model label, format question, new session policy

Hypothesis: Handoffs stay robust when conventions (file form, session policy, model labels)
are recorded instead of discovered per failure.

Intervention: Fixed mislabeled Model: in session file (Claude vs Kimi mixed). Recorded a
paragraph-storage convention in docs/session-handoff.md (unwrapped lines for exact-match).
Added "markdown storage sufficiency" as an open decision in current-state.md — to be
answered after handoff-test evidence, not by default.

Evidence: Live session showed three long-line vs wrapped-paragraph edit failures before a
read/correction; the user asked if markdown is professional for evolving knowledge; model
used was mixed (Claude one round, Kimi otherwise).

Verdict: keep. Next session uses the updated handoff and convention explicitly.

---

## 2026-08-31 — First retention measurement + node 1 taught (model: moonshotai/kimi-k3)

Hypothesis: (a) Presented-only concepts (2026-08-26 scoring feedback) would show some unaided recall after ~5 days; (b) the frozen deep-dive node 1 (crash windows) could be taught to `applied` level in one step-locked session.

Intervention: Ran the owed delayed recall check on all five presented-only concepts BEFORE teaching (learner chose this over teaching directly). Then taught node 1 anchored to socratic-partner's /done flow: definition → lock-in check → learner located the real crash window at the message-send step (duplication-vs-loss trade-off) → second lock-in on why naive retry fails → learner spontaneously generalized to idempotency-as-result-invariant and inferred atomicity's role (node 2) unprompted.

Evidence: Recall check: 0/5 recalled unaided. Crash window partial (kept scope, lost time-gap mechanism); atomicity, least privilege, mocks-reflect-assumptions gone; thundering herd confused with fail-fast queueing. Node 1: learner demonstrated `applied` level unaided (located the window, named the damage mode, explained why retry is wrong, extended to exactly-once semantics in own words). Learner noticed the meta-loop ("repetitions... this is what we're running") — engagement high.

Verdict: keep. (a) Consistent with thesis H1 at n=1 — presentation alone did not retain; logged as evidence, not verdict. The four failed concepts are now `edge` nodes; re-present inside their deep-dive nodes (atomicity = node 2) and re-check with delay. (b) Step-locked teaching to `applied` worked; keep the method. Owed: node-1 recall check ~2026-09-03.
