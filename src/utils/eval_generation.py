import os
from fastapi.testclient import TestClient
from src.main import app
from src.utils.retriever import WeaviateRetriever
import weaviate

client = TestClient(app)

def run():
    print("\n--- Eval: Generation / Grounding ---")

    wclient = weaviate.Client(os.getenv("WEAVIATE_URL", "http://weaviate:8080"))
    schema = wclient.schema.get()
    classes = [c["class"] for c in schema["classes"]]
    assert "Transcript" in classes, "❌ Transcript class missing"
    print("✅ Schema test passed")

    retriever = WeaviateRetriever()
    hits = retriever.retrieve("storytelling", top_k=3)
    assert hits, "❌ No hits for storytelling"
    assert any("hayden" in h["title"].lower() for h in hits), "❌ Expected hayden.txt but not found"
    print("✅ Grounding test passed")

    resp = client.post("/ask", json={"question": "What is the capital of Mars?"})
    data = resp.json()
    assert "I don't know" in data["answer"], "❌ Fallback missing"
    assert data["grounding"] == [], "❌ Grounding should be empty for fallback"
    print("✅ Fallback test passed")

    resp = client.post("/ask", json={"question": "How should I start my video intro?"})
    data = resp.json()
    assert "answer" in data
    assert "grounding" in data
    if data["grounding"]:
        g = data["grounding"][0]
        assert "start_time" in g and "end_time" in g
    print("✅ Integration test passed")
