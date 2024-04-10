from pytube import YouTube
import wget
import os
from pathlib import Path

links = []

with open("videos.txt" ,"r") as file:
    for linha in file:
        links.append(linha.strip())



# Cria a pasta "Engenheiros_do_Hawaii" se ela não existir
pasta_destino = Path("Engenheiros_do_Hawaii")
pasta_destino.mkdir(parents=True, exist_ok=True)



for link in links:
    
    url = link
    video = YouTube(url)

    if("/" in video.title):
        nome = video.title.replace("/"," - ")
    else:
         nome = video.title
         
         
    # Obter o stream de áudio com maior bitrate
    nome = nome + ".mp3"
    caminho_arquivo = pasta_destino / nome
    
    try:
        audio_streams = video.streams.filter(only_audio=True)
        audio_stream = max(audio_streams, key=lambda stream: stream.abr)
        audio_stream.download(output_path=pasta_destino, filename=nome)
        print(f"{nome} 100% \n")
        
    except:
        print(f"erro ao baixar {nome}")

