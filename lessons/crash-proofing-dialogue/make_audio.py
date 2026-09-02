"""Two-voice audio generator for interview/dialogue lessons.

Parses **HOST:** / **MERCED:** speaker tags and renders each line with its own
voice, then stitches the segments into one MP3. Prediction pauses are written
as lines of "... ... ..." and become spoken pauses.
"""

from __future__ import annotations

import asyncio
import re
import tempfile
from pathlib import Path

import edge_tts

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "lesson.md"
OUTPUT = HERE / "lesson.mp3"
TRANSCRIPT = HERE / "transcript.txt"

VOICES = {
    "HOST": "en-US-GuyNeural",
    "MERCED": "en-US-ChristopherNeural",
}
RATE = "-6%"
PAUSE_TEXT = "... ... ..."
# edge-tts cannot synthesize bare dots, and pydub needs ffmpeg (absent here), so pauses
# become a short spoken beat that keeps listeners attentive instead of true silence.
PAUSE_SPOKEN = "Take a second. Answer before I do."


def parse_segments(markdown: str) -> list[tuple[str, str]]:
    """Turn the dialogue markdown into (voice, text) segments."""
    segments: list[tuple[str, str]] = []
    current_speaker = "HOST"
    buffer: list[str] = []

    def flush() -> None:
        text = " ".join(buffer).strip()
        buffer.clear()
        if text:
            segments.append((current_speaker, text))

    for raw in markdown.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line == "---":
            continue
        line = re.sub(r"\*\*([A-Z]+):\*\*\s*", "", line)  # safety: strip tags left in prose
        line = line.replace("**", "").replace("*", "").replace("`", "")
        match = re.match(r"^([A-Z]+):\s*(.*)$", raw.strip().replace("**", ""))
        speaker_match = re.match(r"^(HOST|MERCED):\s*(.*)$", match.group(0) if match else "", )
        if speaker_match:
            flush()
            current_speaker = speaker_match.group(1)
            rest = speaker_match.group(2).strip()
            if rest:
                buffer.append(rest)
            continue
        if line == PAUSE_TEXT:
            flush()
            segments.append((current_speaker, PAUSE_SPOKEN))
            continue
        buffer.append(line)
    flush()
    return segments


async def main() -> None:
    segments = parse_segments(SOURCE.read_text(encoding="utf-8"))
    TRANSCRIPT.write_text(
        "\n\n".join(f"[{speaker}] {text}" for speaker, text in segments) + "\n",
        encoding="utf-8",
    )

    with tempfile.TemporaryDirectory() as tmp:
        with OUTPUT.open("wb") as out:
            for index, (speaker, text) in enumerate(segments):
                if not text:
                    continue
                part = Path(tmp) / f"part_{index:04d}.mp3"
                voice = VOICES.get(speaker, VOICES["HOST"])
                for attempt in range(4):  # edge-tts occasionally drops a segment
                    try:
                        await edge_tts.Communicate(text, voice, rate=RATE).save(str(part))
                        break
                    except Exception:
                        if attempt == 3:
                            raise
                        await asyncio.sleep(2 * (attempt + 1))
                out.write(part.read_bytes())

    words = sum(len(t.split()) for _, t in segments)
    print(f"Segments: {len(segments)} | words: {words} | est. minutes at 140wpm: {words/140:.1f}")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    asyncio.run(main())
