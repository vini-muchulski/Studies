import whisper
import torch

if torch.cuda.is_available():
    print("PyTorch is available on CUDA.")
else:
    print("PyTorch is not available on CUDA.")
    
#https://github.com/openai/whisper

#modelo = whisper.load_model("base")

modelo = whisper.load_model("base", device="cuda")
#modelo = whisper.load_model("base", )

resposta = modelo.transcribe("gravacao.wav")
#é um dicionario

print(resposta["text"])
print("\n ----------- \n")
print(resposta)