
import os
import openai
from openai import OpenAI

openai.api_key = os.getenv("OPENAI_API_KEY")
EMBED_MODEL = os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small")
client = OpenAI()

class OpenAIEmbedder:
    def __init__(self):
        if not openai.api_key:
            raise ValueError("OPENAI_API_KEY not set")

    def embed_text(self, text: str):
        resp = client.embeddings.create(
    model=EMBED_MODEL,
    input=text
        )
        return resp["data"][0]["embedding"]






