import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def enviar_msg(msg):
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role" : "user", "content" : msg}] #orientacoes gerais, ex gpt é professor ou nutri, ver system {"role" : "user"}
    )


    return resposta["choices"][0]["message"]
    #return resposta["choices"][0]["message"]["content"]


print(enviar_msg(" o que foi a apollo 11"))