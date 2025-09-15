# Transcript_Grounded_YouTube_Advisor

A retrieval-augmented chatbot that gives YouTube creators actionable advice grounded **only** in two provided transcripts:

- `aprilynne.txt` → advice on improving video introductions  
- `hayden.txt` → advice on storytelling  

The chatbot uses **Weaviate** for vector storage and **OpenAI** for embeddings + generation.  
Every answer includes **machine-checkable citations** in the format:


If the transcripts do not contain the answer, the bot explicitly responds with  
`"I don't know — the transcripts don't cover that."`

---

## Setup

### 1. Environment

- Python 3.10+ recommended
- Install dependencies:

```bash
pip install -r requirements.txt
