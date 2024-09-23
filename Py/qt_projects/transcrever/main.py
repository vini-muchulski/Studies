import warnings
import whisper

# Ignorar avisos específicos, como FutureWarning
warnings.filterwarnings("ignore", category=FutureWarning)

#https://github.com/openai/whisper/discussions/1185


    
#https://github.com/openai/whisper

#modelo = whisper.load_model("base")
modelo = whisper.load_model("base", device="cuda")
#modelo = whisper.load_model("small", device="cuda")

#base = 1gb vram
#small = 2gb vram

#resposta = modelo.transcribe("gravacao.wav",language="pt", fp16=True)
resposta = modelo.transcribe("audio.wav",language="en")
#é um dicionario

print(resposta["text"])
print("\n ----------- \n")
#print(resposta)