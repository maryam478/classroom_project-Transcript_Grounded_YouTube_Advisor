# src/utils/retriever.py
import os
import weaviate
from typing import List, Dict

WEAVIATE_URL = os.environ.get("WEAVIATE_URL", "http://localhost:8080")
WEAVIATE_CLASS_NAME = os.environ.get("WEAVIATE_CLASS_NAME", "Transcript")

client = weaviate.Client(url=WEAVIATE_URL)


class WeaviateRetriever:
    def __init__(self, class_name=WEAVIATE_CLASS_NAME):
        self.class_name = class_name

    def retrieve(self, query: str, top_k: int = 4) -> List[Dict]:
        from src.utils.embed import OpenAIEmbedder
        embedder = OpenAIEmbedder()
        q_emb = embedder.embed_text(query)
        res = client.query.get(self.class_name, ["title", "text", "chunk_id", "start_time", "end_time"]) \
            .with_near_vector({"vector": q_emb}) \
            .with_limit(top_k) \
            .do()
        hits = []
        raw = res.get("data", {}).get("Get", {}).get(self.class_name, [])
        for h in raw:
            hits.append({
                "title": h.get("title"),
                "text": h.get("text"),
                "chunk_id": h.get("chunk_id"),
                "start_time": h.get("start_time"),
                "end_time": h.get("end_time"),
            })
        return hits
