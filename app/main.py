
from fastapi import FastAPI
from app.routers import auth , audio_file


app = FastAPI()

@app.get("/")
def home():
    return {"hello": "from fastAPI"}

app.include_router(auth.router)
app.include_router(audio_file.router)