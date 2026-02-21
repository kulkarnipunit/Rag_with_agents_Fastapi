from app.models.memory import Memory
from sqlalchemy.orm import Session

class MemoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_memory(self, user_id, content, embedding):
        memory = Memory(
            user_id=user_id,
            content=content,
            embedding=embedding
        )
        self.db.add(memory)
        self.db.commit()
        self.db.refresh(memory)
        return memory

    def get_user_memories(self, user_id):
        return self.db.query(Memory).filter(Memory.user_id == user_id).all()