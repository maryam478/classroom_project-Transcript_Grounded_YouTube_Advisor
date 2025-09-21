# scripts/verify_ingestion.py
import os
import weaviate

WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://weaviate:8080")
WEAVIATE_CLASS_NAME = os.getenv("WEAVIATE_CLASS_NAME", "Transcript")

client = weaviate.Client(url=WEAVIATE_URL)

def main():
    # Show schema
    schema = client.schema.get()
    print("Schema classes:", [c["class"] for c in schema.get("classes", [])])

    # Count total objects
    objs = client.query.get(WEAVIATE_CLASS_NAME, ["title"]).with_limit(10000).do()
    all_objs = objs["data"]["Get"].get(WEAVIATE_CLASS_NAME, [])
    print(f"\nTotal Transcript Chunks: {len(all_objs)}")

    # Count per file
    counts = {}
    for o in all_objs:
        title = o.get("title", "unknown")
        counts[title] = counts.get(title, 0) + 1
    print("\nCounts by transcript file:")
    for title, count in counts.items():
        print(f"- {title}: {count}")

    # Show some samples
    print("\nSample chunks:")
    sample = client.query.get(
        WEAVIATE_CLASS_NAME,
        ["title", "text", "start_time", "end_time"]
    ).with_limit(5).do()

    for s in sample["data"]["Get"][WEAVIATE_CLASS_NAME]:
        print(f"[{s['title']} {s['start_time']}–{s['end_time']}] {s['text'][:80]}...")

if __name__ == "__main__":
    main()
