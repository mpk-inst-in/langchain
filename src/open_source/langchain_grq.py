from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os

load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

api_key = os.environ["GROQ_API_KEY"]
chat = ChatGroq(temperature=0, api_key=api_key, model="llama3-70b-8192")

system = "You are a helpful assistant."
human = "{text}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

chain = prompt | chat
result = chain.invoke(
    {"text": "Which LLM platforms offer the best low latency inference capabilities?"}
)
print(result.content)
