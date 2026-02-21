from app.services.embedding_service import embed_text
from app.services.llm_service import generate_response

class RAGService:

    def __init__(self, repo):
        self.repo = repo

    def chat(self, user_id, message):

        # create embedding for query
        query_embedding = embed_text(message)

        # get relevant memories
        memories = self.repo.get_user_memories(user_id)

        context = "\n".join([m.content for m in memories]) if memories else ""

        prompt = f"""
        Context:
        {context}

        User: {message}
        """

        response = generate_response(prompt)

        return response