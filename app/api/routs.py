from pathlib import Path
import shutil

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

from app.core.config import UPLOAD_DIR
from app.services.whisper_service import transcribe_audio
from app.utils.file_manager import (
    generate_safe_filename,
    is_allowed_file
)
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health():
    return {"status": "running"}