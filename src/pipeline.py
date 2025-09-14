from retriever import Retriever
from llm import call_openai

retriever = Retriever("transcripts")

def ask(question: str, top_k=5) -> str:
    results = retriever.search(question, top_k=top_k)

    context = "\n\n".join(
        f"[source: {r['video']} t={r['start']}–{r['end']}]\n{r['text']}"
        for r in results
    )

    prompt = f"""
Answer the following YouTube advice question.
Use ONLY the context provided below.
Every claim must have at least one citation in the format: [source: <video> t=start–end].
If info is missing, say it's not covered.

Question: {question}

Context:
{context}
"""
    return call_openai(prompt)
