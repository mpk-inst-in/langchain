from dotenv import load_dotenv
import os
import openai
from openai import OpenAI

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()


def get_llm_response(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages, temperature=0
    )

    return response.choices[0].message.content


prompt = "Explain Generative AI in less than 100 words"

result = get_llm_response(prompt, model="gpt-4o-mini")
print(result)
