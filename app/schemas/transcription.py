from pydantic import BaseModel


class TranscriptionResponse(BaseModel):
    """
    Response model returned after successful transcription.
    """

    filename: str
    transcription: str