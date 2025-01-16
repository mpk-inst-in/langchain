from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()


prompt = ChatPromptTemplate.from_template("Tell me a short joke on {subject}")

parser = StrOutputParser()
model = ChatOpenAI(model="gpt-3.5-turbo")
chain = {"subject": RunnablePassthrough()} | prompt | model | parser

for chunk in chain.stream("ice cream"):
    print(chunk, end="", flush=True)
