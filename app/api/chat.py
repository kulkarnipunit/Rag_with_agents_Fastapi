from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.repositories.memory_repo import MemoryRepository
from app.services.rag_service import RAGService

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    user_id: int = 1

@router.post("/message")
def chat(req: ChatRequest, db: Session = Depends(get_db)):

    repo = MemoryRepository(db)
    rag = RAGService(repo)

    response = rag.chat(user_id=req.user_id, message=req.message)

    return {"response": response}