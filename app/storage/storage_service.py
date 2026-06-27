from pathlib import Path
import shutil

from fastapi import UploadFile


def save_uploaded_file(
    file: UploadFile,
    destination: Path
) -> Path:
    """
    Save an uploaded file to the specified destination.

    Args:
        file: Uploaded file received from FastAPI.
        destination: Target path for saving the file.

    Returns:
        Path: Saved file path.
    """

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return destination


def delete_uploaded_file(file_path: Path) -> None:
    """
    Delete a temporary uploaded file.

    Args:
        file_path: Path of the file to remove.
    """

    if file_path.exists():
        file_path.unlink()