"""from pytube import YouTube
import os"""

import os
import yt_dlp

def baixar_video_youtube(url, pasta_destino="."):
    """
    Baixa um vídeo do YouTube na maior qualidade disponível.
    
    Args:
        url (str): A URL do vídeo do YouTube.
        pasta_destino (str): A pasta onde o vídeo será salvo.
    """
    if not os.path.exists(pasta_destino):
        os.mkdir(pasta_destino)
        
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso:
url_do_video = "https://www.youtube.com/watch?v=yPy4lL0fFW0"  # Substitua pela URL do seu vídeo
pasta_de_saida = "./videos_baixados"  # Substitua pela pasta onde deseja salvar o vídeo (crie a pasta)

#cria a pasta caso não exista
if not os.path.exists(pasta_de_saida):
  os.mkdir(pasta_de_saida)

baixar_video_youtube(url_do_video, pasta_de_saida)
