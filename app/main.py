from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, chat, memories, documents
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="Personal Companion AI")

# ✅ CREATE TABLES
Base.metadata.create_all(bind=engine)

# ✅ ADD CORS MIDDLEWARE (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend requests
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ ROUTERS
app.include_router(auth.router, prefix="/auth")
app.include_router(chat.router, prefix="/chat")
app.include_router(memories.router, prefix="/memories", tags=["Memories"])
app.include_router(documents.router, prefix="/documents")

# ✅ HEALTH CHECK
@app.get("/health")
def health():
    return {"status": "ok"}