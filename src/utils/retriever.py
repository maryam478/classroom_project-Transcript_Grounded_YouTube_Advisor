
import os
import weaviate
from typing import List, Dict
from src.utils.embed import OpenAIEmbedder

WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://weaviate:8080")
WEAVIATE_CLASS_NAME = os.getenv("WEAVIATE_CLASS_NAME", "Transcript")

client = weaviate.Client(url=WEAVIATE_URL)

class WeaviateRetriever:
    def __init__(self, class_name: str = WEAVIATE_CLASS_NAME):
        self.class_name = class_name
        self.embedder = OpenAIEmbedder()

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict]:
        q_emb = self.embedder.embed_text(query)
        res = (
            client.query.get(
                self.class_name, ["title", "text", "start_time", "end_time"]
            )
            .with_near_vector({"vector": q_emb})
            .with_limit(top_k)
            .do()
        )
        raw = res.get("data", {}).get("Get", {}).get(self.class_name, [])
        hits = [
            {
                "title": h.get("title"),
                "text": h.get("text"),
                "start_time": h.get("start_time"),
                "end_time": h.get("end_time"),
            }
            for h in raw
        ]
        return hits


