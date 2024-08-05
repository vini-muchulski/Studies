from dotenv import load_dotenv
import os
from google.cloud import aiplatform # type: ignore

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_google_vertexai import ChatVertexAI
from langchain_core.prompts import ChatPromptTemplate 

aiplatform.init(project="langgemini2")
load_dotenv()
chave_api = os.getenv("GOOGLE_API_KEY")
#print(chave_api)



"""mensagens = [
    SystemMessage("responda a pergunta em portugues"),
    HumanMessage("fale sobre o que foi a apollo 11"),
]"""

modelo = ChatVertexAI(model="gemini-1.5-flash",project_id="langgemini2")
parser = StrOutputParser()
chain = modelo | parser

#resposta = modelo.invoke(mensagens)
#texto = parser.invoke(resposta)

template_mensagem = ChatPromptTemplate.from_messages([
    ("system","responda a pergunta em  {idioma}"),
    ("human","{texto}")
])

chain = template_mensagem | modelo | parser

#texto = chain.invoke({"idioma":"portugues","texto":"fale sobre o que foi a apollo 11"})
#print(texto)