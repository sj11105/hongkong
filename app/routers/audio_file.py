from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os
from datetime import datetime

router = APIRouter()

AUDIO_UPLOAD_DIR = "uploaded_audios"
os.makedirs(AUDIO_UPLOAD_DIR, exist_ok=True)


ALLOWED_AUDIO_TYPES = [
    "audio/mpeg", "audio/wav", "audio/x-wav", "audio/mp3",
    "audio/x-m4a", "audio/webm", "application/octet-stream"
]

@router.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    
    print("DEBUG: File content type ->", file.content_type)
    print("DEBUG: File name ->", file.filename)
    
    
    file_ext = os.path.splitext(file.filename)[1]
    print("DEBUG: File extension ->", file_ext)

    # Check for valid MIME type
    if file.content_type not in ALLOWED_AUDIO_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type: {file.content_type}. Only audio files are allowed."
        )

    # Save with timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{file.filename}"
    file_path = os.path.join(AUDIO_UPLOAD_DIR, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return JSONResponse(
        content={
            "filename": filename,
            "saved_path": file_path,
            "mime_type": file.content_type,
            "message": "File uploaded successfully"
        }
    )
