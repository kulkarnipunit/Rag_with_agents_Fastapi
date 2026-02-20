from app.services.embedding_service import embed_text
from app.services.vector_store import search
from app.services.llm_service import generate_response


class RagService:

    def chat(self, query):

        query_embedding = embed_text(query)

        context = search(query_embedding)

        return generate_response(query, context)