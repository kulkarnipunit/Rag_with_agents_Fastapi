from fastapi import APIRouter
from app.services.rag_service import RagService

router = APIRouter()

@router.post("/message")
def chat(message: str):

    rag = RagService()

    response = rag.chat(message)

    return {"response": response}