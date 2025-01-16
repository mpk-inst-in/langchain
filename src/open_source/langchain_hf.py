from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate
import os

# huggingface inference apis

load_dotenv()

print(os.environ["HF_TOKEN"])
model_id = "meta-llama/Llama-3.2-1B-Instruct"

llm_api = HuggingFaceEndpoint(
    repo_id=model_id,
    task="text-generation",
    max_new_tokens=1000,
    do_sample=False,
    temperature=1,
)

chat_llama = ChatHuggingFace(llm=llm_api)

PROMPT = "Explain {subject} in 100 words"

prompt = ChatPromptTemplate.from_template(PROMPT)
chain = prompt | llm_api

response = chain.invoke({"subject": "Generative AI"})

print(response)
