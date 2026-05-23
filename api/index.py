from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os

app = FastAPI()

# Vercel Environment Variable theke API Key nebe
API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

class PromptInput(BaseModel):
    user_prompt: str

@app.post("/api/ask-ai")
async def ask_ai_backend(data: PromptInput):
    try:
        response = model.generate_content(data.user_prompt)
        return {"ai_response": response.text}
    except Exception as e:
        return {"error": str(e)}
