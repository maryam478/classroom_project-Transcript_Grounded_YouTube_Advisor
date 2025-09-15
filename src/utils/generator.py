# src/utils/generator.py
import os
import openai
from typing import List

openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

SYSTEM_PROMPT = (
    "You are an assistant that answers creator questions using ONLY the provided transcript context."
    " For each specific claim or recommendation, attach a citation of the format "
    "[source: <filename> t=HH:MM:SS–HH:MM:SS]. If the transcripts don't contain the answer, say "
    "'I don't know — the transcripts don't cover that.' Do not hallucinate."
)

class OpenAIGenerator:
    def __init__(self):
        if not openai.api_key:
            raise ValueError("OPENAI_API_KEY not set")

    def generate(self, question: str, hits: List[dict]) -> str:
        # Build context with explicit citation lines per chunk
        context_parts = []
        for h in hits:
            citation = f"[source: {h['title']} t={h['start_time']}–{h['end_time']}]"
            context_parts.append(f"{citation}\n{h['text']}")
        context = "\n\n---\n\n".join(context_parts)

        user_prompt = (
            f"QUESTION:\n{question}\n\nCONTEXT (only use this context to answer):\n{context}\n\n"
            "Provide actionable recommendations. After each recommendation, include the citation(s) "
            "in the exact format [source: filename t=HH:MM:SS–HH:MM:SS]. If the context doesn't contain "
            "the answer, reply: \"I don't know — the transcripts don't cover that.\""
        )

        resp = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=512,
            temperature=0.0,
        )
        return resp["choices"][0]["message"]["content"].strip()
