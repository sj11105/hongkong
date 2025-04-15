import google.generativeai as genai
import textwrap
from decouple import config

MAX_CHAR_LENGTH = 10000  
CHUNK_WRAP = 9000        
GEMINI_MODEL = "models/gemini-1.5-flash"
GEMINAI_API = config("GEMINI_API")

genai.configure(api_key=GEMINAI_API)

model = genai.GenerativeModel(GEMINI_MODEL)

def summarize_chunk(chunk: str) -> str:
    prompt = (f"""You are an AI meeting assistant. This is a multilingual transcript (English + Chinese + others) analyse it properly.\n
      Please after analyzing the transcript generate summary in a structured way which includes the brief overview of topic , key action points
      and keep it clear and limit it upto one page only.
      Transcript:
      \"\"\"{chunk}\"\"\"
      """)


    response = model.generate_content(prompt)
    return response.text

def summarize_large_transcript(transcript: str) -> str:
    if len(transcript) <= MAX_CHAR_LENGTH:
        return summarize_chunk(transcript)

    #split transcript into chunks
    chunks = textwrap.wrap(transcript, CHUNK_WRAP, break_long_words=False, replace_whitespace=False)

    summaries = []
    for idx, chunk in enumerate(chunks):
        print(f"Summarizing chunk {idx+1}/{len(chunks)}...")
        summary = summarize_chunk(chunk)
        summaries.append(summary.strip())

    # Combine all partial summaries into a final one
    final_prompt =  (f"You are an AI assistant. These are summaries of different parts of a multilingual meeting.\n\n"
    f"Please combine them into one single-page summary report with main discussion points and action items. "
    f"Keep it clear and concise.\n\n"
    f"Summaries:\n\n"
    f"{chr(10).join(summaries)}")

    final_response = model.generate_content(final_prompt)
    return final_response.text
