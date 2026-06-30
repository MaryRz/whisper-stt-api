from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException,
)

from app.core.config import UPLOAD_DIR
from app.storage.storage_service import (
    save_uploaded_file,
    delete_uploaded_file,
)
from app.services.whisper_service import transcribe_audio
from app.utils.file_manager import (
    generate_safe_filename,
    is_allowed_file,
)

from app.schemas.transcription import TranscriptionResponse

router = APIRouter(tags=["Speech To Text"])


@router.get("/")
def health():
    return {"status": "running"}


@router.post(
    "/transcribe",
    summary="Transcribe an audio file",
    response_model=TranscriptionResponse,
)

async def transcribe_audio_endpoint(
    file: UploadFile = File(...)
):
    """
    Upload an audio file and return its transcription.
    """

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is missing.",
        )

    if not is_allowed_file(file.filename):
        raise HTTPException(
            status_code=400,
            detail="Unsupported audio format.",
        )

    safe_filename = generate_safe_filename(file.filename)
    file_path = UPLOAD_DIR / safe_filename

    try:
        save_uploaded_file(
            file=file,
            destination=file_path,
        )

        text = transcribe_audio(str(file_path))

        return {
            "filename": safe_filename,
            "transcription": text,
        }

    finally:
        delete_uploaded_file(file_path)