Transcript-Grounded YouTube Advisor 🎬🤖

A small but production-minded chatbot that gives creators practical advice on how to improve their YouTube channel, grounded only in the provided video transcripts (aprilynne.txt and hayden.txt).

The system uses:

Weaviate → Vector database for storing transcript chunks

OpenAI → Embeddings + LLM to generate grounded answers

FastAPI → Lightweight web API

CLI interface → Quick local testing

All answers include citations pointing to the specific transcript and timestamp ranges used.

📂 Project Structure
├─ README.md
├─ DESIGN.md
├─ requirements.txt
├─ transcripts/
│   ├─ aprilynne.txt
│   └─ hayden.txt
├─ scripts/
│   ├─ ingestion-script.py
│   └─ verify_ingestion.py
├─ src/
│   ├─ main.py
│   ├─ routes/
│   │   └─ ask.py
│   └─ utils/
│       ├─ preprocessor.py
│       ├─ chunk.py
│       ├─ embed.py
│       ├─ retriever.py
│       ├─ generator.py
│       ├─ eval.py
│       ├─ eval_generation.py
│       ├─ eval_bertscore.py
│       └─ eval_judge.py
└─ tests/
    ├─ test_schema.py
    ├─ test_grounding.py
    ├─ test_fallback.py
    └─ test_integration.py

⚙️ Setup
1. Environment variables

Create a .env file in the root:

OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
WEAVIATE_URL=http://weaviate:8080
WEAVIATE_CLASS_NAME=Transcript

2. Install dependencies (if running locally without Docker)
python3 -m venv yt_myenv
source yt_myenv/bin/activate
pip install -r requirements.txt

🐳 Running with Docker Compose

We use Docker Compose to spin up both Weaviate and the chatbot container.

1. Build & start services
docker compose up -d --build


Weaviate will be available on http://localhost:8080

FastAPI app will be available on http://localhost:8000

2. Ingest transcripts into Weaviate
docker compose exec app python scripts/ingestion-script.py


Verify ingestion:

docker compose exec app python scripts/verify_ingestion.py


Expected output:

Schema classes: ['Transcript']

Total Transcript Chunks: ~2800

Counts by transcript file:
- aprilynne.txt: ~1200
- hayden.txt: ~1600

💻 Usage
CLI Mode

Ask a question directly from the command line:

=> docker compose exec app python src/main.py --q "What storytelling techniques help with retention?"
=> docker compose exec app python src/main.py --q "How should I start my video intro?"
=> docker compose exec app python src/main.py --q "What does Hayden say about improving retention?"
=> docker compose exec app python src/main.py --q "What thumbnail strategies did Aprilynne mention?"



Example output:

🤖 Bot Answer:
- Use curiosity loops and narrative beats to sustain engagement. [source: hayden.txt t=00:01:00–00:01:03]

📖 Sources:
- hayden.txt [00:01:00–00:01:03]
- aprilynne.txt [00:04:21–00:04:23]

API Mode

Run the app without args:

docker compose exec app python src/main.py


Then query via curl:

curl -s -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "How should I start my video intro?"}'


Response:

{
  "answer": "Start with a hook that matches your title and thumbnail ... [source: aprilynne.txt t=00:06:23–00:06:30]",
  "grounding": [
    {"title": "aprilynne.txt", "start_time": "00:06:23", "end_time": "00:06:30"}
  ]
}
