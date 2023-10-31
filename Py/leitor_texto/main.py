from gtts import gTTS
import os

texto = "ola mundo e planeta terra"

linguagem = "pt"

tts = gTTS(texto, lang=linguagem)
tts.save("ola.mp3")


#os.system('ffplay -autoexit ola.mp3')
os.system('ffplay -autoexit -nodisp ola.mp3')

