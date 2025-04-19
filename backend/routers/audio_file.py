from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
import uuid
from backend.llm import whisper , genai
from backend.utils import pdf_convert


router = APIRouter()

""" AUDIO_UPLOAD_DIR = "uploaded_audios"
os.makedirs(AUDIO_UPLOAD_DIR, exist_ok=True) """


ALLOWED_AUDIO_TYPES = [
    "audio/mpeg",    # .mp3
    "audio/wav",     # .wav
    "audio/x-wav",   # .wav 
    "audio/mp3",     # .mp3 
    "audio/x-m4a",   # .m4a
    "audio/webm",    # .webm
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # This is where the this files reside
APP_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))  # one directory back 
AUDIO_DIR = os.path.join(APP_DIR, "newaudio") 

@router.post("/upload-audio/")
async def upload_audio(file: UploadFile = File(...)):
    print("received request for audio transcribe")

    try:
        print("Receiving files")
        os.makedirs(AUDIO_DIR, exist_ok=True)
        audio_path = os.path.join(AUDIO_DIR, f"{uuid.uuid4()}_{file.filename}")
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

        summary_text = genai.summarize_large_transcript(transcription)
        
        pdf_path = pdf_convert.save_summary_pdf_to_pdfhub(summary_text, os.path.basename(audio_path))
        pdf_filename = os.path.basename(pdf_path) 
        return JSONResponse(content={
            "transcription": transcription,
            "summary": summary_text,
            "download_url": f"{pdf_filename}"
        })
    
    except Exception as e:
        print(f"Error during transcription: {str(e)}")
        return JSONResponse(status_code=500, content={"error": str(e)})