from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from keys import API_KEY


def get_top_5_videos(query):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    try:
        # Realiza a busca
        search_response = youtube.search().list(
            q=query,
            type='video',
            part='id,snippet',
            maxResults=5  # Limitamos a 5 resultados
        ).execute()

        video_ids = [item['id']['videoId'] for item in search_response['items']]

        # Obtém as estatísticas dos vídeos
        videos_response = youtube.videos().list(
            id=','.join(video_ids),
            part='statistics,snippet'
        ).execute()

        # Cria uma lista com informações dos 5 vídeos mais relevantes
        top_videos = []
        for video in videos_response['items']:
            video_info = {
                'title': video['snippet']['title'],
                'video_id': video['id'],
                'view_count': int(video['statistics'].get('viewCount', 0)),
                'url': f'https://www.youtube.com/watch?v={video["id"]}'
            }
            top_videos.append(video_info)

        # Ordena os vídeos por número de visualizações (do maior para o menor)
        top_videos.sort(key=lambda x: x['view_count'], reverse=True)

        return top_videos

    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")
        return None

# Exemplo de uso
query = "skank ainda gosto dela"
results = get_top_5_videos(query)

if results:
    print(f"Top 5 vídeos para a busca '{query}':")
    for i, video in enumerate(results, 1):
        print(f"\n{i}. {video['title']}")
        print(f"   Visualizações: {video['view_count']}")
        print(f"   URL: {video['url']}")
else:
    print("Não foi possível encontrar vídeos.")
    
    
    
if results:
    url = results[0]["url"]
    print(f"URL do vídeo mais visto: {url}")

    # Configuração para abrir o Chrome com a extensão
    extension_path = 'C:\\Users\\Cliente\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\gighmmpiobklfepjocnamgkkbiglidom\\6.6.0_0'
    options = Options()
    options.add_argument(f'--load-extension={extension_path}')
    
    driver = webdriver.Chrome(options=options)
    
    # Guarda o ID da janela principal
    janela_principal = driver.current_window_handle
    
    # Abre a URL do vídeo
    driver.get(url)
    #driver.refresh()
    #janela_principal.send_keys(Keys.SPACE)
    # Espera para garantir que todas as janelas sejam abertas
    
    # Fecha todas as janelas exceto a principal
    for window_handle in driver.window_handles:
        if window_handle != janela_principal:
            driver.switch_to.window(window_handle)
            driver.close()
    
    # Volta para a janela principal
    driver.switch_to.window(janela_principal)
    driver.refresh()
    
    # Aqui você pode adicionar mais código para interagir com a página do vídeo
    
    input("Pressione Enter para fechar o navegador...")
    driver.quit()
else:
    print("Nenhum vídeo encontrado.")