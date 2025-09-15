# tests/test_fallback.py
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_fallback_unknown():
    r = client.post("/ask", json={"question": "What's the weather in Paris today?"})
    assert r.status_code == 200
    data = r.json()
    # We expect either explicit "I don't know" or empty grounding
    assert data["grounding"] == [] or "don't know" in data["answer"].lower()
