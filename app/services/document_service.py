import fitz  # PyMuPDF
from app.services.embedding_service import embed_text
from app.services.vector_store import store_vector

async def process_pdf(file):

    content = await file.read()
    doc = fitz.open(stream=content, filetype="pdf")

    chunks = []

    for page in doc:
        text = page.get_text()
        chunks.append(text)

    for chunk in chunks:
        embedding = embed_text(chunk)
        store_vector(chunk, embedding)

    return {"message": "PDF processed"}