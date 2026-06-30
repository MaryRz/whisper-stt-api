from fastapi import FastAPI
from app.api.routes import router
from app.exceptions.handlers import register_exception_handlers

app = FastAPI(
    title="Whisper STT API",
    version="1.0.0",
    description="Production-ready Speech-to-Text API using OpenAI Whisper"
)

app.include_router(router)
register_exception_handlers(app)