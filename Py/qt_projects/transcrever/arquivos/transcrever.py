import whisper
import torch

#https://github.com/openai/whisper/discussions/1185

if torch.cuda.is_available():
    print("PyTorch is available on CUDA.")
else:
    print("PyTorch is not available on CUDA.")
    
#https://github.com/openai/whisper

#modelo = whisper.load_model("base")

#modelo = whisper.load_model("base", device="cuda")
#modelo = whisper.load_model("base", )
modelo = whisper.load_model("small", device="cuda")
#resposta = modelo.transcribe("gravacao.wav",language="pt", fp16=True)
resposta = modelo.transcribe("gravacao.wav",language="en")
#é um dicionario

print(resposta["text"])
print("\n ----------- \n")
print(resposta)