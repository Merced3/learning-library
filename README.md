# Learning System (working name — rename freely)

A personal system for getting brought up to speed on anything, and staying current as it changes. One learner, one trusted interface, many verified sources.

**Start here:** `AGENTS.md`, then `docs/thesis.md`. **New session?** Use the prompt in `docs/session-handoff.md`.

## Layout

```text
AGENTS.md            # the stable spine + rules (read first)
docs/
  thesis.md          # the goal, the two-axis model of knowledge, hypotheses
  learner.md         # what we know about how this mind learns (editable by the learner)
  current-state.md   # what exists, what's next — always honest
  decision-log.md    # append-only experiments: hypothesis → evidence → verdict
  session-handoff.md # new-session prompt + closing checklist
lessons/             # audio/other lesson artifacts (one subfolder per topic)
maps/                # per-topic edge maps (created when first teaching happens)
sessions/            # per-topic teaching session logs (created when teaching happens)
tools/
  make_audio.py      # lesson.md → transcript.txt + lesson.mp3
```

Everything except `AGENTS.md` is a current best theory and may be rewritten — with the change logged in `docs/decision-log.md`.
