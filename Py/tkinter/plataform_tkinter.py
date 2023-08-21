import platform
import socket
from datetime import datetime
import getpass
from time import sleep

from tkinter import *

#project with python that show some informations about your pc




def get_infos():
    

    texto_1["text"] = "NOME DA MAQUINA = "+ platform.node()
    texto_2["text"] = "ARQUITETURA = ", platform.architecture()


    texto_3["text"] = "SO = "+ platform.system()
    texto_4["text"] = "Versao Sistema Operacional = "+ platform.release()
    texto_5["text"] = "Processador = "+ platform.processor()
    texto_6["text"] = "Versão Python = "+ platform.python_version()

    ip = socket.gethostbyname(socket.gethostname())
    texto_7["text"] = "IP = " + ip

    texto_8["text"] = "Hora local =  ", datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    texto_9["text"] = "User = "+getpass.getuser()

    texto_10["text"] = " "

    

    

def salvar_arquivo():
    with open("arquivo_info.txt", "a") as arquivo:

        infos_lista = []
        nome_machine = "NOME DA MAQUINA........",platform.node()
        arq = "ARQUITETURA............",platform.architecture()


        so = "SO.....................",platform.system()
        version = "versao so..............",platform.release()
        amd = "processador............",platform.processor()
        py_version = "versao do python.......",platform.python_version()

        ip = socket.gethostbyname(socket.gethostname())
        ip_maquina = f"IP.....................{ip}"
        #print(ip_maquina)

        hora = "Hora local.............", datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        usuario = "User...................",getpass.getuser()

        infos_lista.append(nome_machine)
        infos_lista.append(arq)
        infos_lista.append(so)
        infos_lista.append(version)
        infos_lista.append(amd)
        infos_lista.append(py_version)
        infos_lista.append(hora)
        infos_lista.append(usuario)

        arquivo.write("\n")
        for elemento in infos_lista:
            id = elemento[0]
            info = elemento[1]

            palavra = str(id) + " " + str(info)
            arquivo.write(palavra)
            arquivo.write("\n")

        arquivo.write(ip_maquina)
        arquivo.write("\n")
        arquivo.close()
        
        texto_10["text"] = "Arquivo gerado na pasta!"
        
        

        


     





root = Tk()

root.title("Platformo INFO")
root.geometry("600x500")

texto_orientacao = Label(root,text="Visualize as informações da sua maquina")
texto_orientacao.grid(column=0,row=1,padx=10,pady=10)

botao = Button(root,text="Mostrar",command=get_infos)
botao.grid(column=0,row=2,padx=10,pady=10)

botao_salvar = Button(root,text="Salvar",command=salvar_arquivo)
botao_salvar.grid(column=1,row=2,padx=10,pady=10)

texto_10 = Label(root, text="")
texto_10.grid(column=1,row=3,padx=10,pady=10)
    


#array_textos = []
#for i in range(1,10):
    #texto = Label(root, text="")
    #texto.grid(column=0,row=2+i,padx=10,pady=10)


texto_1 = Label(root, text="")
texto_1.grid(column=0,row=3,padx=10,pady=10)

texto_2 = Label(root, text="")
texto_2.grid(column=0,row=4,padx=10,pady=10)

texto_3 = Label(root, text="")
texto_3.grid(column=0,row=5,padx=10,pady=10)

texto_4 = Label(root, text="")
texto_4.grid(column=0,row=6,padx=10,pady=10)

texto_5 = Label(root, text="")
texto_5.grid(column=0,row=7,padx=10,pady=10)

texto_6 = Label(root, text="")
texto_6.grid(column=0,row=8,padx=10,pady=10)

texto_7 = Label(root, text="")
texto_7.grid(column=0,row=9,padx=10,pady=10)

texto_8 = Label(root, text="")
texto_8.grid(column=0,row=10,padx=10,pady=10)

texto_9 = Label(root, text="")
texto_9.grid(column=0,row=11,padx=10,pady=10)


root.mainloop()


