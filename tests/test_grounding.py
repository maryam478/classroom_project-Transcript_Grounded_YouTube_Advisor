# tests/test_grounding.py
from src.utils.retriever import WeaviateRetriever

def test_retrieve_aprilynne():
    r = WeaviateRetriever()
    hits = r.retrieve("first sentence should meet the expectations set by the title", top_k=3)
    assert isinstance(hits, list)
    assert any("aprilynne.txt" in (h.get("title") or h.get("source")) for h in hits)
