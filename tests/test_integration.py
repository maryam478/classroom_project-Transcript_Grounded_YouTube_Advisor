from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_integration_post():
    response = client.post("/ask", json={"question": "How do I improve my intros?"})
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "grounding" in data
    # If grounding exists, check timestamps
    if data["grounding"]:
        g = data["grounding"][0]
        assert "start_time" in g
        assert "end_time" in g
