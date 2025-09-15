# scripts/ingestion-script.py
import os
import glob
import re
import json
from dotenv import load_dotenv
from tqdm import tqdm
import weaviate
from src.utils.preprocessor import preprocess_text
from src.utils.chunk import chunk_segments_with_timestamps
from src.utils.embed import OpenAIEmbedder

load_dotenv()

WEAVIATE_URL = os.environ.get("WEAVIATE_URL", "http://localhost:8080")
WEAVIATE_CLASS_NAME = os.environ.get("WEAVIATE_CLASS_NAME", "Transcript")

client = weaviate.Client(url=WEAVIATE_URL)
embedder = OpenAIEmbedder()

# Ensure class exists (simple schema)
schema = {
    "classes": [
        {
            "class": WEAVIATE_CLASS_NAME,
            "vectorizer": "none",
            "properties": [
                {"name": "title", "dataType": ["text"]},
                {"name": "text", "dataType": ["text"]},
                {"name": "source", "dataType": ["text"]},
                {"name": "chunk_id", "dataType": ["text"]},
                {"name": "start_time", "dataType": ["text"]},
                {"name": "end_time", "dataType": ["text"]},
            ],
        }
    ]
}

existing = client.schema.get()
if WEAVIATE_CLASS_NAME not in [c.get("class") for c in existing.get("classes", [])]:
    client.schema.create(schema)

transcript_files = glob.glob(os.path.join("transcripts", "*.txt"))

batch = client.batch()
batch.batch_size = 25

def parse_webvtt_blocks(text):
    """Return list of dicts: {'start','end','text'} by parsing WEBVTT timestamps."""
    lines = text.splitlines()
    blocks = []
    i = 0
    # find lines with timestamp pattern
    ts_re = re.compile(r"(\d{2}:\d{2}:\d{2}\.\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}\.\d{3})")
    while i < len(lines):
        m = ts_re.search(lines[i])
        if m:
            start, end = m.groups()
            i += 1
            text_lines = []
            while i < len(lines) and lines[i].strip() != "":
                text_lines.append(lines[i])
                i += 1
            blocks.append({"start": start[:8], "end": end[:8], "text": " ".join(text_lines).strip()})
        else:
            i += 1
    return blocks

for path in tqdm(transcript_files, desc="ingest transcripts"):
    title = os.path.basename(path)
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    cleaned = preprocess_text(raw)
    # parse into timestamped blocks
    blocks = parse_webvtt_blocks(cleaned)
    # chunk blocks into overlapping chunks of ~500 words while preserving timestamps
    chunks = chunk_segments_with_timestamps(blocks, chunk_size_words=450, chunk_overlap_words=80)
    for i, c in enumerate(chunks):
        emb = embedder.embed_text(c["text"])
        properties = {
            "title": title,
            "source": title,
            "text": c["text"],
            "chunk_id": f"{title}::chunk::{i}",
            "start_time": c["start"],
            "end_time": c["end"],
        }
        batch.add_data_object(properties, WEAVIATE_CLASS_NAME, vector=emb)
batch.flush()
print("Ingestion complete.")
