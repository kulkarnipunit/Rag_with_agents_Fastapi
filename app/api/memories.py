from fastapi import APIRouter, Depends
from app.dependencies.db_dep import get_db
from app.repositories.memory_repo import MemoryRepository
from app.services.memory_service import MemoryService

router = APIRouter()

@router.post("/")
def store_memory(content: str, db = Depends(get_db)):

    repo = MemoryRepository(db)
    service = MemoryService(repo)

    return service.store_memory(user_id=1, content=content)