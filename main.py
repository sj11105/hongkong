import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset
from pydub import AudioSegment
import io
import soundfile as sf
import numpy


device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-tiny"

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

dataset = load_dataset("distil-whisper/librispeech_long", "clean", split="validation")
sample = dataset[0]["audio"]  # This is a dict with "array" and "sampling_rate"

# buffer = io.BytesIO()
# sf.write(buffer, sample["array"], sample["sampling_rate"], format="WAV")
# buffer.seek(0)

# # Load into pydub
# audio = AudioSegment.from_file(buffer, format="wav")
# audio = audio[:30 * 1000]  # Slice first 30 seconds

result = pipe(sample)
print(result["text"])
