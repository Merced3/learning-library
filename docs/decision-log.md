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
