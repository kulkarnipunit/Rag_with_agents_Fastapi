from app.services.embedding_service import embed_text

class MemoryService:

    def __init__(self, repo):
        self.repo = repo

    def store_memory(self, user_id, content):
        embedding = embed_text(content)
        return self.repo.create_memory(user_id, content, str(embedding))