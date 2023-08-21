import requests
from tkinter import *



def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_dolar = float(cotacao_dolar)
    #cotacao_dolar = "{:.2f}".format(cotacao_dolar)

    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_euro = float(cotacao_euro)
    #cotacao_euro = "{:.2f}".format(cotacao_euro)

    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

    texto = f"Dolar = {cotacao_dolar} \nEuro = {cotacao_euro} \nBTC = {cotacao_btc}"

    #print(texto)
    #return texto
    texto_cotacoes["text"] = texto




janela = Tk()
janela.title("Cotação - DOLAR - EURO - BTC")
janela.geometry("200x200")
texto_orientacao = Label(janela, text="Clique para mostrar as cotações")
texto_orientacao.grid(column=0,row=1,padx=10,pady=10)



botao = Button(janela,text="Atualizar Valores",command=pegar_cotacoes)
botao.grid(column=0,row=4,padx=10,pady=10)


texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0,row=3,padx=10,pady=10)

janela.mainloop()