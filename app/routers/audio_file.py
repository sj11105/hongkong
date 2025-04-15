from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
import uuid
from app.llm import whisper

router = APIRouter()

AUDIO_UPLOAD_DIR = "uploaded_audios"
os.makedirs(AUDIO_UPLOAD_DIR, exist_ok=True)


ALLOWED_AUDIO_TYPES = [
    "audio/mpeg", "audio/wav", "audio/x-wav", "audio/mp3",
    "audio/x-m4a", "audio/webm", "application/octet-stream"
]

@router.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    print("received request for audio transcribe")

    try:
        print("Receiving files")
        os.makedirs("newaudio", exist_ok=True)
        audio_path = os.path.join("newaudio", f"{uuid.uuid64()}_{file.filename}")
        print(f"saving audio to {audio_path}")

        with open(audio_path , "wb") as f:
            data = await file.read()
            print(f"audio size is {len(data)} bytes")
            f.write(data)

        if not os.path.exists(audio_path):
            raise Exception("File was not saved successfully.")
        
        chunks = whisper.split_audio(audio_path)

        print("Starting transcription")
        transcription = whisper.transcribe_chunks(chunks)

        return JSONResponse(content={"transcription": transcription})

    
    except Exception as e:
        print(f"Error during transcription: {str(e)}")
        return JSONResponse(status_code=500, content={"error": str(e)})