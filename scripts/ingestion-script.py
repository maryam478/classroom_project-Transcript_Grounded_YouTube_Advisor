import os
import glob
import re
import weaviate
from dotenv import load_dotenv
from tqdm import tqdm
from src.utils.embed import OpenAIEmbedder

load_dotenv()

WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://weaviate:8080")
WEAVIATE_CLASS_NAME = os.getenv("WEAVIATE_CLASS_NAME", "Transcript")

client = weaviate.Client(url=WEAVIATE_URL)

# 🧹 Reset schema on every run
try:
    client.schema.delete_all()
    print("🧹 Old schema cleared")
except Exception as e:
    print("⚠️ Could not clear schema:", e)

schema = {
    "classes": [
        {
            "class": WEAVIATE_CLASS_NAME,
            "vectorizer": "none",  # we provide embeddings
            "properties": [
                {"name": "title", "dataType": ["text"]},
                {"name": "text", "dataType": ["text"]},
                {"name": "start_time", "dataType": ["text"]},
                {"name": "end_time", "dataType": ["text"]},
            ],
        }
    ]
}
client.schema.create(schema)

embedder = OpenAIEmbedder()


def parse_transcript(path, merge_lines=5):
    """Parse SRT/WebVTT transcript into chunks of ~merge_lines."""
    segments = []
    with open(path, "r") as f:
        lines = [l.strip() for l in f]

    i = 0
    buffer = []
    start_time, end_time = None, None

    while i < len(lines):
        # Skip numeric index lines
        if re.match(r"^\d+$", lines[i]):
            i += 1
            continue

        # Match timestamp line
        ts_match = re.match(
            r"(\d{2}:\d{2}:\d{2}(?:[.,]\d{1,3})?)\s*-->\s*(\d{2}:\d{2}:\d{2}(?:[.,]\d{1,3})?)",
            lines[i],
        )
        if ts_match:
            # If buffer already has text from previous block, flush it
            if buffer and start_time:
                segments.append((start_time, end_time, " ".join(buffer)))
                buffer = []
            start_time = ts_match.group(1).split(".")[0]
            end_time = ts_match.group(2).split(".")[0]
            i += 1
            continue

        # Collect caption text lines
        if lines[i]:
            buffer.append(lines[i])
            if len(buffer) >= merge_lines and start_time:
                segments.append((start_time, end_time, " ".join(buffer)))
                buffer = []
        else:
            # Blank line = end of caption block → flush buffer
            if buffer and start_time:
                segments.append((start_time, end_time, " ".join(buffer)))
                buffer = []
        i += 1

    # Flush last buffer
    if buffer and start_time:
        segments.append((start_time, end_time, " ".join(buffer)))

    return segments



# === Ingest transcripts ===
for path in tqdm(glob.glob("transcripts/*.txt"), desc="ingest transcripts"):
    title = os.path.basename(path)
    segments = parse_transcript(path)

    for seg in segments:
        start, end, text = seg
        emb = embedder.embed_text(text)
        client.data_object.create(
            {
                "title": title,
                "text": text,
                "start_time": start,
                "end_time": end,
            },
            class_name=WEAVIATE_CLASS_NAME,
            vector=emb,
        )
        print(f"Inserted: {title} [{start}–{end}] {text[:80]}...")

print("✅ Ingestion complete with SRT/WebVTT support + chunk merging")
