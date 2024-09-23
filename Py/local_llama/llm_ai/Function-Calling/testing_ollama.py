from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# https://github.com/samwit/agent_tutorials/blob/main/ollama_agents/llama3_local/llama3_ollama_functions.py
# Local Llama3 
llm = ChatOllama(
    model="llama3",
    keep_alive=-1, # keep the model loaded indefinitely
    temperature=0,
    max_new_tokens=512)

prompt = ChatPromptTemplate.from_template("Escreva-me um artigo de 200 palavras sobre {topic} sob a perspectiva de um {profession}. falar apenas em português do Brasil. ")

# using LangChain Expressive Language chain syntax
chain = prompt | llm | StrOutputParser()

#print(chain.invoke({"topic": "LLMs", "profession": "shipping magnate"}))

for chunk in chain.stream({"topic": "LLMs", "profession": "piloto de aviao"}):
    print(chunk, end="", flush=True)