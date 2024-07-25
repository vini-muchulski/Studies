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

resposta = modelo.transcribe("instagram.mp4", language='pt')
#é um dicionario


arquivo =  open("transcricao_nvidia.txt","w", encoding="utf-8")
arquivo.write(resposta["text"])
    
print(resposta["text"])
print("\n ----------- \n")
print(resposta)