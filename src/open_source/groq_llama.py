from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

groq_key = os.environ["GROQ_API_KEY"]
print(groq_key)
groq_client = Groq(api_key=groq_key)


def get_llm_response(prompt, model="llama-3.3-70b-versatile"):
    messages = [{"role": "user", "content": prompt}]
    chat_completion = groq_client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=0,
    )
    return chat_completion.choices[0].message.content


prompt = "Explain Generative AI in 100 words."

response = get_llm_response(prompt)

print(response)
