from fastapi import APIRouter, UploadFile, File
from app.services.document_service import process_pdf

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    return await process_pdf(file)