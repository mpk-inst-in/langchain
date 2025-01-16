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

res = chain.invoke("ice cream")
print(res)
