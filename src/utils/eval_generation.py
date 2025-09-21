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
    if "Transcript" not in classes:
        print("❌ Transcript class missing in schema")
        return
    print("✅ Schema test passed")

    retriever = WeaviateRetriever()
    hits = retriever.retrieve("storytelling", top_k=3)
    if not hits:
        print("❌ No hits for storytelling (retriever issue)")
        return
    if not any("hayden" in h["title"].lower() for h in hits):
        print("❌ Expected hayden.txt but not found in hits")
        print("Hits returned:", hits)
        return
    print("✅ Grounding test passed")

    # Fallback test
    resp = client.post("/ask", json={"question": "What is the capital of Mars?"})
    data = resp.json()
    if "I don't know" not in data.get("answer", ""):
        print("❌ Fallback missing")
        print("Bot actually answered:", data)
        return
    if data.get("grounding") != []:
        print("❌ Grounding should be empty for fallback")
        print("Bot grounding was:", data.get("grounding"))
        return
    print("✅ Fallback test passed")

    # Integration test
    resp = client.post("/ask", json={"question": "How should I start my video intro?"})
    data = resp.json()
    if "answer" not in data:
        print("❌ Integration test failed, no 'answer' field")
        print("Response:", data)
        return
    if "grounding" not in data:
        print("❌ Integration test failed, no 'grounding' field")
        print("Response:", data)
        return
    if data["grounding"]:
        g = data["grounding"][0]
        if "start_time" not in g or "end_time" not in g:
            print("❌ Integration grounding missing timestamps")
            print("Grounding entry:", g)
            return
    print("✅ Integration test passed")

    print("\n🎉 All generation checks passed!")
