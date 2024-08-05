from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI


load_dotenv()
os.getenv("OPENAI_API_KEY")
chave_api = os.getenv("OPENAI_API_KEY")

mensagens = [
    SystemMessage("traduza o texto a seguir para ingles"),
    HumanMessage("fale sobre o que foi a apollo 11"),
]

modelo = ChatOpenAI(model="gpt-3.5-turbo")

resposta = modelo.invoke(mensagens)
print(resposta)