from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st


st.title("Local LLaMa 3.1")
template = """Question: {question}

Answer: Let's think and explain the concept"""

prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="llama3.1")

chain = prompt | model

question = st.chat_input("Digite sua questao")


st.write(chain.invoke({"question": question}))

