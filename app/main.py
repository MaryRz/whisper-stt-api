from fastapi import FastAPI, UploadFile, File
import os

from app.services.whisper_service import transcribe_audio

app = FastAPI(
    title="Whisper STT API",
    version="0.1.0"
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def root():
    return {
        "project": "Whisper STT API",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    text = transcribe_audio(file_path)

    return {
        "filename": file.filename,
        "transcription": text
    }