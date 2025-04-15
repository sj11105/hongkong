from fastapi import UploadFile, File, FastAPI
from fastapi.responses import JSONResponse
import uuid
import os

app = FastAPI()

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    print("📥 Received request to /transcribe/")

    try:
        print(f"📂 Incoming file: {file.filename}")

        # Create tmp directory if not exists
        os.makedirs("tmp", exist_ok=True)

        # Save file to tmp folder
        audio_path = os.path.join("tmp", f"{uuid.uuid4()}_{file.filename}")
        print(f"📄 Saving audio to: {audio_path}")

        with open(audio_path, "wb") as f:
            data = await file.read()
            print(f"📦 Audio size: {len(data)} bytes")
            f.write(data)

        if not os.path.exists(audio_path):
            raise Exception("❌ File was not saved successfully.")

        print("🔪 Splitting audio into chunks...")
        # chunks = split_audio(audio_path)
        # transcription = transcribe_chunks(chunks)

        print("✅ Transcription completed.")
        return JSONResponse(content={"transcription": "Yeah it's working"})

    except Exception as e:
        print(f"❗Error during transcription: {str(e)}")
        return JSONResponse(status_code=500, content={"error": str(e)})
