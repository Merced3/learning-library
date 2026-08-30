"""Turn an audio-friendly Markdown lesson into a transcript and MP3."""

from __future__ import annotations

import argparse
import asyncio
import re
from pathlib import Path

import edge_tts

DEFAULT_VOICE = "en-US-GuyNeural"
DEFAULT_RATE = "-8%"


def markdown_to_speech(markdown: str) -> str:
    """Remove visual Markdown while retaining readable spoken structure."""
    text = re.sub(r"```.*?```", "", markdown, flags=re.DOTALL)
    text = re.sub(r"^---+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^>\s?", "", text, flags=re.MULTILINE)
    text = re.sub(r"^[-*+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\d+[.)]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"!\[([^]]*)]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^]]+)]\([^)]+\)", r"\1", text)
    text = text.replace("**", "").replace("__", "").replace("`", "")
    text = text.replace("├──", "").replace("└──", "").replace("│", "")
    text = text.replace("→", " then ").replace("↓", " then ")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a clean transcript and MP3 from a Markdown lesson."
    )
    parser.add_argument("source", type=Path, help="Path to the Markdown lesson")
    parser.add_argument("--voice", default=DEFAULT_VOICE, help="Microsoft Edge TTS voice")
    parser.add_argument("--rate", default=DEFAULT_RATE, help="Speaking rate, such as -8%% or +5%%")
    parser.add_argument("--transcript", type=Path, help="Transcript output path")
    parser.add_argument("--output", type=Path, help="MP3 output path")
    return parser.parse_args()


async def create_audio(args: argparse.Namespace) -> None:
    source = args.source.resolve()
    if not source.is_file():
        raise SystemExit(f"Lesson source does not exist: {source}")

    transcript_path = (args.transcript or source.with_name("transcript.txt")).resolve()
    output_path = (args.output or source.with_name("lesson.mp3")).resolve()
    transcript_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    transcript = markdown_to_speech(source.read_text(encoding="utf-8"))
    transcript_path.write_text(transcript, encoding="utf-8")
    await edge_tts.Communicate(transcript, args.voice, rate=args.rate).save(str(output_path))

    words = len(transcript.split())
    print(f"Transcript: {transcript_path}")
    print(f"Audio: {output_path}")
    print(f"Words: {words:,} (about {words / 145:.1f} minutes at 145 words/minute)")


def main() -> None:
    asyncio.run(create_audio(parse_args()))


if __name__ == "__main__":
    main()
