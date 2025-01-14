from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

chatgpt = ChatOpenAI(model="gpt-4o-mini", temperature=0)

PROMPT = "Explain {topic} in two minutes."

prompt = ChatPromptTemplate.from_template(PROMPT)

chain = prompt | chatgpt

response = chain.invoke({"topic": "Generative AI"})

print(response.content)
