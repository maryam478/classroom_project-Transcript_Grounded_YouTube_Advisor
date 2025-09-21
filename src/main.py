# src/main.py
import argparse
import uvicorn
from fastapi import FastAPI, Body
from src.utils.retriever import WeaviateRetriever
from src.utils.generator import OpenAIGenerator

# Initialize components
retriever = WeaviateRetriever()
generator = OpenAIGenerator()
app = FastAPI(title="Transcript-Grounded YouTube Advisor")

# ---------------------------
# CLI entrypoint
# ---------------------------
def cli():
    parser = argparse.ArgumentParser(description="Transcript-Grounded YouTube Advisor")
    parser.add_argument("--q", type=str, help="Question to ask the chatbot")
    args = parser.parse_args()

    if args.q:
        hits = retriever.retrieve(args.q, top_k=5)
        answer, grounding = generator.generate(args.q, hits)

        print("🤖 Bot Answer:\n", answer)
        print("\n📖 Sources:")
        for g in grounding:
            print(f"- {g['title']} [{g['start_time']}–{g['end_time']}]")
    else:
        print("Please provide a question with --q")

# ---------------------------
# API entrypoint
# ---------------------------
@app.post("/ask")
def ask_endpoint(payload: dict = Body(...)):
    question = payload.get("question")
    if not question:
        return {"error": "Missing 'question' field"}

    hits = retriever.retrieve(question, top_k=5)
    answer, grounding = generator.generate(question, hits)
    return {"answer": answer, "grounding": grounding}

# ---------------------------
# Entrypoint
# ---------------------------
if __name__ == "__main__":
    import sys

    # If run with args → CLI mode
    if len(sys.argv) > 1:
        cli()
    else:
        # Otherwise run as API
        uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=False)
        
        
#         OUTPUT
        
#         "What storytelling techniques help with retention?"

# 🤖 Bot Answer:
#  Storytelling techniques that enhance retention often involve engaging the audience through compelling narratives and relatable content. Techniques mentioned include:

# 1. **High engagement strategies**: Developing content that captivates the audience’s attention and keeps them interested throughout the video or story. Aprilynne notes the importance of understanding the strategies behind high retention videos [source: aprilynne.txt t=00:01:00–00:01:03].

# 2. **Structured storytelling**: Encouraging the use of structured narratives, possibly similar to techniques used by notable creators, can help in maintaining audience interest. Hayden suggests looking up to established storytelling methods for inspiration on how to tell stories effectively [source: hayden.txt t=00:52:14–00:52:17].

# 3. **Data-driven insights**: Using data to inform storytelling strategies can lead to better retention by understanding what parts of the story resonate most with viewers. Hayden mentions the importance of using retention and data for improving content strategies [source: hayden.txt t=00:07:03–00:07:04].

# By leveraging these techniques, storytellers can create more engaging content that retains viewer attention effectively.

# 📖 Sources:
# - aprilynne.txt [00:01:00–00:01:03]
# - hayden.txt [01:10:10–01:10:12]
# - hayden.txt [00:52:14–00:52:17]
# - aprilynne.txt [00:04:21–00:04:23]
# - hayden.txt [00:07:03–00:07:04]
# (/Users/maryamsyeda/Desktop/classroom_project-Transcript_Grounded_YouTube_Advisor/yt_myenv) maryamsyeda@mac classroom_project-Transcript_Grounded_YouTube_Advisor % 

