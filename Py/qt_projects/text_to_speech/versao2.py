from gtts import gTTS
import os

texto = "salve salve"

linguagem = "pt"

#tts = gTTS(texto, lang=linguagem)

tts = gTTS(text=texto) # Gera um áudio com a fala "Olá, mundo!" em português do Brasil, em velocidade lenta.
tts.save("salve.mp3")


#os.system('ffplay -autoexit ola.mp3')
os.system('ffplay -autoexit -nodisp salve.mp3')




