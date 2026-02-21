from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.memory_service import MemoryService
from app.repositories.memory_repo import MemoryRepository

router = APIRouter()

@router.post("/")
def store_memory(content: str, db: Session = Depends(get_db)):
    repo = MemoryRepository(db)
    service = MemoryService(repo)
    return service.store_memory(user_id=1, content=content)