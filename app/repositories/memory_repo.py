from app.models.memory import Memory


class MemoryRepository:

    def __init__(self, db):
        self.db = db

    def get_user_memories(self, user_id: int):
        return self.db.query(Memory).filter(Memory.user_id == user_id).all()

    def create_memory(self, user_id: int, content: str, embedding: str):
        memory = Memory(
            user_id=user_id,
            content=content,
            embedding=embedding
        )

        self.db.add(memory)
        self.db.commit()
        self.db.refresh(memory)

        return memory