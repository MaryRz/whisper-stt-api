from pathlib import Path
from uuid import uuid4


def generate_safe_filename(original_filename: str) -> str:
    """
    Generate a unique and safe filename while preserving
    the original file extension.
    """
    extension = Path(original_filename).suffix.lower()

    return f"{uuid4()}{extension}"

ALLOWED_EXTENSIONS = {
    ".wav",
    ".mp3",
    ".m4a",
    ".flac",
    ".ogg"
}


def is_allowed_file(filename: str) -> bool:
    """
    Check whether the uploaded file extension is supported.
    """
    extension = Path(filename).suffix.lower()

    return extension in ALLOWED_EXTENSIONS