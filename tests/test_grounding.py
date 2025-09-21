# tests/test_grounding.py
import pytest
from src.utils.retriever import WeaviateRetriever

def test_grounding_has_timestamps():
    retriever = WeaviateRetriever()
    hits = retriever.retrieve("intro", top_k=1)
    if hits:  # only run if data ingested
        hit = hits[0]
        assert "start_time" in hit
        assert "end_time" in hit
        assert isinstance(hit["start_time"], str)
        assert isinstance(hit["end_time"], str)
