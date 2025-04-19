from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from backend.routers import auth , audio_file , download_pdf


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
     allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"hello": "from fastAPI"}

app.include_router(auth.router)
app.include_router(audio_file.router)
app.include_router(download_pdf.router)

