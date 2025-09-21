import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run():
    print("\n--- Eval: LLM Judge ---")
    answer = "Start strong with your title in the intro. [source: aprilynne.txt t=00:06:19–00:06:37]"
    context = "aprilynne.txt [00:06:19–00:06:37]: Start strong by aligning your intro with your title."
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Judge if the answer is grounded in the context. Reply Yes or No."},
            {"role": "user", "content": f"Answer: {answer}\nContext: {context}"}
        ]
    )
    verdict = resp.choices[0].message.content.strip().lower()
    print(f"Judge verdict: {verdict}")
    assert "yes" in verdict, "❌ Judge says answer not grounded"
    print("✅ LLM Judge test passed")
