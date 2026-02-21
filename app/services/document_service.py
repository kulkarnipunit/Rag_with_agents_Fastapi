import fitz
from app.services.embedding_service import embed_text

async def process_pdf(file):
    contents = await file.read()

    return {
        "status": "processed",
        "size": len(contents)
    }