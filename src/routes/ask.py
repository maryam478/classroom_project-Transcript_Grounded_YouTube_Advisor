# src/routes/ask.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.utils.retriever import WeaviateRetriever
from src.utils.generator import OpenAIGenerator

router = APIRouter()

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    answer: str
    grounding: list

retriever = WeaviateRetriever()
generator = OpenAIGenerator()

@router.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    if not req.question.strip():
        raise HTTPException(status_code=400, detail="Empty question")

    hits = retriever.retrieve(req.question, top_k=5)
    if not hits:
        return {"answer": "I don't know — transcripts don’t cover that.", "grounding": []}
    answer = generator.generate(req.question, hits)
    return {"answer": answer, "grounding": hits}
