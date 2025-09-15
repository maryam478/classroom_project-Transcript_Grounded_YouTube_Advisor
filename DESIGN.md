
---

## `DESIGN.md`

```markdown
# Design Notes

## Architecture

- **Ingestion**
  - Parse WebVTT transcripts → timestamped blocks
  - Chunk into ~500-word windows with ~80-word overlap
  - Generate embeddings (OpenAI `text-embedding-3-small`)
  - Store in Weaviate with metadata: `title`, `chunk_id`, `start_time`, `end_time`, `text`

- **Retrieval**
  - Embed user query with OpenAI
  - Retrieve `top_k=4` nearest chunks from Weaviate
  - Return metadata including timestamps for grounding

- **Generation**
  - Prompt LLM with:
    - Question
    - Context = retrieved chunks + citations
  - System prompt enforces:
    - Use only provided context
    - Every recommendation must include `[source: file t=start–end]`
    - If unsupported → answer `"I don't know"`

- **Interface**
  - FastAPI `/ask` endpoint returning JSON:
    ```json
    {
      "answer": "...",
      "grounding": [
        {"title": "aprilynne.txt", "chunk_id": "...", "start_time": "00:06:19", "end_time": "00:06:37", "text": "..."}
      ]
    }
    ```
  - CLI wrapper for convenience

- **Evaluation**
  - Unit tests:
    - Schema presence
    - Grounding correctness (e.g. intro guidance → aprilynne)
    - Fallback outside scope
  - Simple `eval.py` harness runs example prompts and prints pass/fail

---

## Tradeoffs

- **LLM model choice**: Used `gpt-4o-mini` instead of larger GPT-4 for cost and latency; still strong at citation-following.
- **Chunking strategy**: Word-based overlapping chunks (simple, avoids cutting timestamps mid-sentence); downside: some duplication.
- **No reranking**: Direct nearest-neighbor search for simplicity; might retrieve off-topic chunks occasionally.
- **Timestamps granularity**: Citations use start/end of chunk, not per-sentence; simpler but less precise.
- **Evaluation scope**: Only light tests; no human-judge eval or BERTScore (out of assignment timebox).

---

## Known Limitations

- Possible redundancy in answers if multiple overlapping chunks are cited.
- Precision of citations limited to chunk boundaries.
- System doesn’t currently verify that LLM-produced citations match the evidence text (trusts the model to use provided ones).
- Requires manual `.env` setup for API keys.

---

## Future Extensions

- Add semantic reranker (e.g. cross-encoder) before generation.
- Automatic post-processing to validate citations against retrieved snippets.
- Add a small React or Streamlit UI for demo.
- Expand dataset and scale retrieval infra (sharding, hybrid BM25+vector).
