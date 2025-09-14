import re
from pathlib import Path

def parse_srt_like(file_path: str):
    """
    Parse an SRT-like transcript into chunks:
    returns list of dicts: {video, start, end, text}
    """
    entries = []
    video = Path(file_path).stem

    with open(file_path, "r", encoding="utf-8") as f:
        raw = f.read().strip()

    pattern = re.compile(r"(\d+)\n(\d{2}:\d{2}:\d{2}\.\d+) --> (\d{2}:\d{2}:\d{2}\.\d+)\n(.+?)(?=\n\d+\n|\Z)", re.S)
    matches = pattern.findall(raw)

    for idx, (num, start, end, text) in enumerate(matches):
        text = " ".join(line.strip() for line in text.split("\n"))
        entries.append({
            "video": video,
            "start": start,
            "end": end,
            "text": text
        })

    return entries

def load_all_transcripts(folder="transcripts"):
    all_entries = []
    for f in Path(folder).glob("*.txt"):
        all_entries.extend(parse_srt_like(str(f)))
    return all_entries
