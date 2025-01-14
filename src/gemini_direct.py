import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
import os

gemini_key = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=gemini_key)

model = genai.GenerativeModel(model_name="gemini-1.5-pro")
response = model.generate_content(
    "What makes llms so fast in providing responses to complex prompts?"
)

print(response.text)
