# # src/utils/generator.py
# import os
# from openai import OpenAI

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# SYSTEM_PROMPT = """
# You are a helpful assistant. 
# Ground every answer in transcript text. 
# Always include citations in this format:
# [source: <title> t=<start_time>–<end_time>]
# """

# class OpenAIGenerator:
#     def generate(self, question: str, hits: list):
#         context = "\n\n".join(
#             [f"{h['title']} [{h.get('start_time')}–{h.get('end_time')}]: {h['text']}" for h in hits]
#         )
#         resp = client.chat.completions.create(
#             model=MODEL,
#             messages=[
#                 {"role": "system", "content": SYSTEM_PROMPT},
#                 {"role": "user", "content": f"Q: {question}\n\nContext:\n{context}"},
#             ],
#             max_tokens=400,
#         )
#         return resp.choices[0].message.content

# src/utils/generator.py
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

SYSTEM_PROMPT = """
You are a helpful assistant.
Ground every answer in transcript text.
Always include citations in this format:
[source: <title> t=<start_time>–<end_time>]
"""

class OpenAIGenerator:
    def generate(self, question: str, hits: list):
        if not hits:
            return "🤖 Bot: I don't know — transcripts don’t cover that.", []

        # Build context string from retrieved transcript chunks
        context = "\n\n".join(
            f"{h['title']} [{h['start_time']}–{h['end_time']}]: {h['text']}"
            for h in hits
        )

        # Call OpenAI with question + context
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Q: {question}\n\nContext:\n{context}"},
            ],
            max_tokens=400,
        )

        answer = resp.choices[0].message.content.strip()

        # Build grounding metadata to return alongside the answer
        grounding = [
            {
                "title": h["title"],
                "start_time": h["start_time"],
                "end_time": h["end_time"],
            }
            for h in hits
        ]

        return answer, grounding


