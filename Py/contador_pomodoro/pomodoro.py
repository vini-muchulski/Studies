import time

from tkinter import *

#from playsound import *
import pygame


"""

tempo = int(input('Digite tempo em segundos: '))

for i in range(tempo,0,-1):
    segundos = tempo % 60
    minutos  = int(tempo/60) % 60
    horas = int(tempo/3600) 

    print(f"horas {horas} - minutos {minutos} - segundos {segundos}")
    tempo = tempo -1
    time.sleep(0.01)



print("fim")

"""

def pomodoro():
    tempo = int(minutos_pomo.get())*60 + int(segundos_pomo.get())

    pygame.mixer.init()

    for i in range(tempo,0,-1):
        segundos = tempo % 60
        minutos  = int(tempo/60) % 60
        horas = int(tempo/3600) 

        print(f"horas {horas} - minutos {minutos} - segundos {segundos}")
        tempo = tempo -1
        

        minutos_pomo.set(minutos)
        segundos_pomo.set(segundos)

        time.sleep(1)
        root.update()

        if(tempo == 0):
            
           
            estude = Label(root,font=("arial",15,"bold"),text="Intervalo ",bg="#000",fg="#D6D6D6")
            estude.place(x=280,y=170)
            minutos_pomo.set("00")
            segundos_pomo.set("00")
            root.update()

            
            #playsound("zap_song.mp3")
            # Carrega o arquivo de áudio
            pygame.mixer.music.load('zap_song.mp3')

            # Reproduz o arquivo de áudio
            pygame.mixer.music.play()

            


    


root = Tk()

root.title("Pomodoro")
root.geometry("500x500")
root.config(bg="#000")
root.resizable(False,False
               )
texto_orientacao = Label(root,text="Pomodoro",font="arial 30 bold",bg="#000",fg="#D6D6D6")
texto_orientacao.grid(column=0,row=1,padx=10,pady=10)


Label(root,font=("arial",15,"bold"),text="Tempo atual: ",bg="#000",fg="#D6D6D6").place(x=30,y=75)

estude = Label(root,font=("arial",15,"bold"),text="Estude ",bg="#000",fg="#D6D6D6")
estude.place(x=280,y=170)

#timer

minutos_pomo = StringVar()
Entry(root,textvariable=minutos_pomo,width=2,font="arial 30 bold").place(x=30,y=155)
minutos_pomo.set("00")
Label(root,font=("arial",10,"bold"),text="minutos ",bg="#000",fg="#D6D6D6").place(x=25,y=115)

segundos_pomo = StringVar()
Entry(root,textvariable=segundos_pomo,width=2,font="arial 30 bold").place(x=100,y=155)
segundos_pomo.set("00")
Label(root,font=("arial",10,"bold"),text="segundos ",bg="#000",fg="#D6D6D6").place(x=85,y=115)

btn = Button(root,text="Iniciar",bg="#000",fg="#fff",width=20,height=2,font="arial 10 bold",command=pomodoro)
btn.grid(column=1,row=3,padx=10,pady=10)

root.mainloop()