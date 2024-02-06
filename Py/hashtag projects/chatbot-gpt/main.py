import openai
from keys import api_key
# https://www.youtube.com/watch?v=vGn4yAsIpkU


chave_api = api_key
openai.api_key = chave_api


def enviar_msg(msg,lista_msgs=[]):
    lista_msgs.append({"role" : "user", "content" : msg})
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=lista_msgs #orientacoes gerais, ex gpt é professor ou nutri, ver system {"role" : "user"}
    )


    return resposta["choices"][0]["message"]
    #return resposta["choices"][0]["message"]["content"] #retorna so a resposta


lista_msgs = []
while True:
    texto = input("Mande sua mensagem: ")

    if(texto == "sair"):
        break
    else:
        
        resposta = enviar_msg(texto,lista_msgs=lista_msgs)
        lista_msgs.append(resposta)
        resposta_normalizada = resposta["content"]
        print(f"ChatBot: {resposta_normalizada}")