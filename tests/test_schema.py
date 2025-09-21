# tests/test_schema.py
import os, weaviate
import os, weaviate
import pytest

WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://weaviate:8080")
WEAVIATE_CLASS_NAME = os.getenv("WEAVIATE_CLASS_NAME", "Transcript")
client = weaviate.Client(url=WEAVIATE_URL)

def test_class_exists():
    schema = client.schema.get()
    classes = [c["class"] for c in schema["classes"]]
    assert WEAVIATE_CLASS_NAME in classes

def test_class_has_timestamp_fields():
    schema = client.schema.get()
    transcript_class = next(c for c in schema["classes"] if c["class"] == WEAVIATE_CLASS_NAME)
    props = [p["name"] for p in transcript_class["properties"]]
    assert "start_time" in props
    assert "end_time" in props


