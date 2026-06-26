from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Whisper STT API",
    version="1.0.0",
    description="Production-ready Speech-to-Text API using OpenAI Whisper"
)

app.include_router(router)