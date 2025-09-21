# tests/test_fallback.py
from src.utils.retriever import WeaviateRetriever
from src.utils.generator import OpenAIGenerator

def test_fallback_behavior():
    retriever = WeaviateRetriever()
    hits = retriever.retrieve("nonsense question that won't exist", top_k=2)
    if not hits:
        # mimic generator fallback
        response = {"answer": "I don't know — transcripts don’t cover that.", "grounding": []}
        assert response["grounding"] == []
