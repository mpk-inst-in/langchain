import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
gemini = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

PROMPT = "Explain {topic} in two minutes."

prompt = ChatPromptTemplate.from_template(PROMPT)

chain = prompt | gemini

response = chain.invoke({"topic": "Generative AI"})

print(response.content)
