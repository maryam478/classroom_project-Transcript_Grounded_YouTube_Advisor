# tests/test_schema.py
import os
import weaviate

WEAVIATE_URL = os.environ.get("WEAVIATE_URL", "http://localhost:8080")
WEAVIATE_CLASS_NAME = os.environ.get("WEAVIATE_CLASS_NAME", "Transcript")

client = weaviate.Client(url=WEAVIATE_URL)

def test_class_exists():
    schema = client.schema.get()
    classes = [c.get("class") for c in schema.get("classes", [])]
    assert WEAVIATE_CLASS_NAME in classes
