from fastapi import FastAPI
from app.api import auth, chat, memories

from app.db.session import engine
from app.db.base import Base
from app.models.memory import Memory
from app.api import documents

app = FastAPI(title="Personal Context AI")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth")
app.include_router(chat.router, prefix="/chat")
app.include_router(memories.router, prefix="/memories")
app.include_router(documents.router, prefix="/documents")

@app.get("/health")
def health():
    return {"status": "ok"}