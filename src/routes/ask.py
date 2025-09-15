# src/routes/ask.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.utils.retriever import WeaviateRetriever
from src.utils.generator import OpenAIGenerator

router = APIRouter()

class AskRequest(BaseModel):
    question: str

class GroundHit(BaseModel):
    title: str
    chunk_id: str
    start_time: str
    end_time: str
    text: str

class AskResponse(BaseModel):
    answer: str
    grounding: list[GroundHit]

retriever = WeaviateRetriever()
generator = OpenAIGenerator()

@router.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    q = req.question.strip()
    if not q:
        raise HTTPException(status_code=400, detail="Empty question")
    hits = retriever.retrieve(q, top_k=5)
    if not hits:
        return {"answer": "I don't know — the transcripts don't cover that.", "grounding": []}
    answer = generator.generate(q, hits)
    return {"answer": answer, "grounding": hits}
