from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

model_name = "meta-llama/Llama-3.2-1B-Instruct"

hf_key = os.environ["HF_TOKEN"]

client = InferenceClient(model=model_name, api_key=hf_key)

chat = [{"role": "user", "content": "Explain Generative AI in 200 words."}]

response = client.chat_completion(chat, max_tokens=1000)

print(response.choices[0].message.content)
