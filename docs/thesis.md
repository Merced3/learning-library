# Thesis

## The goal

> Given any domain where the learner is behind, bring them to current working competence
> quickly — and keep their knowledge current as the domain itself changes.

The motivating paraphrase (DHH on the Lex Fridman Podcast, #474, 2025 — **the appearance and the skeptic-to-convert arc are verified; the specific "away for a year, caught up in two weeks" wording is unverified**): after a year away from a fast-moving field, AI could bring him back up to speed in about two weeks.

The learner's own clarification sharpens this: **even if the quote were verified, one person's experience is not evidence.** The real thesis is not "copy DHH's result" — it is:

> AI is maximally personalized. Use that to gain and retain as much knowledge as possible,
> through whatever discipline the learner actually responds to — and verify it by
> stress-testing the learner on what they *supposedly* just learned.

Many people read ten books on a subject and retain fragments. This system aims for the opposite shape: whatever the intake (reading, listening, watching, doing), new knowledge is deliberately stressed — retrieval, application, unannounced re-testing — until it survives. What survives the stress is `known`. What doesn't goes back to `edge`.

## What this system is NOT

- Not a course. A course is fixed content for a crowd. This is fitted to one mind and must survive the content itself going stale.
- Not a content generator. Producing an audio lesson, quiz, or summary is logistics. The product is a demonstrated, durable capability in the learner.
- Not a fixed method. Audio lessons, Socratic dialogue, worked examples, retrieval drills, projects — all are interchangeable modalities. The loop decides; the modality serves.

## The two-axis model of "what the learner knows"

Every knowledge claim tracked by this system has two independent states:

**Mastery axis** (does the learner hold it?):

| state | meaning |
| --- | --- |
| `unknown` | no evidence of contact |
| `edge` | partially held; the frontier where teaching is most efficient |
| `known` | demonstrated — with the evidence level recorded (see AGENTS.md) |
| `blocked` | cannot be assessed yet (missing prerequisite or context) |

**Epistemic axis** (is it still true in the world?):

| state | meaning |
| --- | --- |
| `current as of <date>` | believed true, with source, as of a date |
| `contested` | credible conflicting information exists |
| `superseded` | replaced by a newer claim; keep the old one visible |

The epistemic axis exists because domains rot. "What you know" is only half the record; "whether it's still true" is the other half. Re-checking stale claims is a first-class system job, not an accident.

## Working hypotheses (to be tested, not believed)

1. **H1 — Audio is orientation, not retention.** Long audio lessons build vocabulary and a map, but do not produce durable recall without retrieval practice. *(Basis: learner's own report that audio "wasn't a good way to retain." Evidence: pending.)*
2. **H2 — Edge-of-understanding pacing beats comprehensiveness.** Teaching exactly at the `edge` (per the Alvar method) will out-perform broad surveys per unit of learner effort. *(Research anchor: Bloom's "2-sigma problem" (1984) — one-to-one mastery tutoring outperformed classroom teaching by roughly two standard deviations; later replications found smaller effects, so treat as directional support, not gospel. Believed-true as of 2026-08 from training knowledge, not live-verified.)*
3. **H3 — One trusted interface beats many sources.** Fewer interfaces, more verified sources behind them, reduces the trust-hedging tax on learning.
4. **H4 — Public knowledge artifacts are motivating.** A shareable, evidence-backed record of competence (an upgrade on the resume) may motivate upkeep — but must never leak the private record. *(Parked: no build until the private loop works.)*
5. **H5 — Unprompted spaced retrieval beats re-exposure.** Randomly-timed questions about recently-learned material, delivered through the learner's normal chat surface, will retain more per minute than re-reading or re-listening. *(Basis: retrieval-practice research is strong generally; whether the learner tolerates unprompted pings is unknown and must be tested gently — defaults off, opt-in, low frequency first.)*
6. **H6 — Communication surfaces are interchangeable.** Discord is the learner's current home for agent interaction and likely the first channel — but it is an adapter, not the system. The retention loop asks questions; *where* the question appears must be swappable (Discord, terminal, web, whatever exists next) without touching learning logic. Relatedly: the learner's existing question-asking agent (socratic-partner) may someday serve as one questioning surface — an integration to evaluate later, not a dependency now.

## What would change our mind

- If the learner demonstrably retains from passive listening alone (delayed unaided recall), H1 falls and audio-first becomes the cheap default.
- If probing costs more motivation than it saves, shorten probes and let quizzes inside teaching do the mapping.
- If tracking the epistemic axis proves to be bookkeeping nobody reads, collapse it to re-verification events only.
