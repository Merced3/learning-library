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

---

## 2026-09-01 — Node 2 taught (transactions/atomicity) + grounding examples in the real codebase (model: moonshotai/kimi-k3)

Hypothesis: (a) Node 2 could be anchored on the learner's own 2026-08-31 inference ("crash can't split the write") and brought to at least `explained` in one step-locked session; (b) a self-generated concept (idempotency, coined by the learner on 2026-08-31) would survive ~1 day unaided.

Intervention: Probed first (crash between CLOSING-write and billing-write; learner correctly predicted duplication/loss, guessed transaction = smaller window). Taught atomicity as "harmless, not smaller" (rollback makes the crash window unable to split the pair). Lock-in 1: what the DB shows after a crash mid-transaction. Lock-in 2: credit-charge design (boundary + placement). Final check: order COMPLETE / archive / Discord-post with per-gap damage modes. On learner request, verified all claims against the real socratic-partner repo before grading.

Evidence: (a) Succeeded at `explained`: lock-in 1 answered correctly but self-flagged as a protective guess, then mechanism explained in own words; boundary selection correct unaided; placement before/after the point-of-no-return needed coaching (clean "I really don't know" edge signal); final ordering check mixed — mislabeled the retry-safe archive gap as unrecoverable, correctly flagged the Discord-send gap as unknown-delivery. (b) FAILED: learner asked "what does idempotency mean again?" after ~1 day, then re-derived instantly on re-presentation. New observed bias: treats "gap has bad outcome" as "wrong answer" — logged in learner.md. Repo grounding: store.py uses `with self._connection()` transaction boundaries (rollback on exception); CLOSING + reopen_conversation is the reset/retry mechanism; real /done order is CLOSING → LLM → send message → final DB write, with reopen-on-failure.

Verdict: keep. Node 2 graded `known (explained)`; applied not yet clean → re-check with delay ~2026-09-03 alongside node-1 recheck. Idempotency failure is n=2 against "self-generation retains" — consistent with H1/H5; re-present idempotency at node 5 with delayed check. Grounding synthetic examples in the real repo is cheap and high-trust; adopt as default whenever a real anchor exists.

OUTCOME (same-day addendum): Learner chose to keep pushing node 2 toward `applied` in the same session. Applied re-test (order the full /done sequence with damage modes, scope the charge transaction, walk the crash-retry): damage-mode naming was correct per boundary (applied-level); envelope scope wrong (put CLOSING + LLM call inside the transaction); retry walk double-charged (missed the keyed skip-check). Corrections: rollback only reaches the DB (outside-world actions can never live in a transaction); each DB step is its own envelope; guarded writes (`WHERE status='OPEN'`) as the real-code idempotency pattern; record-exists → balance-was-decremented proof chain. Final proof question not answered unaided — learner hit a fatigue wall and stopped ("Im pretty spent"). Diagram-first explanation (one boxed 5-step picture) landed where paragraphs hadn't. Grade stays `explained`; fresh proof re-run owed next session before node 3. Fatigue wall + interrupt desire logged in learner.md.
