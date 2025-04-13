import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset
from pydub import AudioSegment
import io
import soundfile as sf
import numpy
import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
AUDIO_DIR = BASE_DIR / "uploaded_audios"

# Get all audio files (you can add filters like *.wav or *.mp3)
audio_files = sorted(AUDIO_DIR.glob("*.*"))  # You can also use "*.wav" or "*.mp3"

if not audio_files:
    raise FileNotFoundError("No audio files found in the directory.")

# Pick the first audio file
first_audio_path = audio_files[3]
print(f"First audio file found: {first_audio_path.name}")

# Load the audio content into a variable
with open(first_audio_path, "rb") as f:
    audio_data = f.read()
    

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-base"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    device=device,
    return_timestamps=True
)

#dataset = load_dataset("distil-whisper/librispeech_long", "clean", split="validation")
sample = audio_data

result = pipe(sample)


print(result["text"]) 
