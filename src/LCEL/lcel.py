from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

chatgpt = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

PROMPT = "{query}"

prompt = ChatPromptTemplate.from_template(PROMPT)

llm_chain = prompt | chatgpt

response = llm_chain.invoke({"query": "Explain the math behind machine learning."})

print(response.content)
