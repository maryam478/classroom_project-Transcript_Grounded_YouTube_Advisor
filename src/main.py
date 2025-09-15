# src/main.py
from fastapi import FastAPI
from src.routes.ask import router as ask_router

app = FastAPI(title="Transcript Grounded YouTube Advisor")
app.include_router(ask_router, prefix="", tags=["ask"])

@app.get("/health")
def health():
    return {"status": "ok"}
