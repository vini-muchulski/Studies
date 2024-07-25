from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def converter_views_para_inteiro(views_texto):
    if not views_texto:
        return 0

    # Remove palavras desnecessárias e espaços extras
    views_texto = views_texto.lower().replace("visualizações", "").replace("de", "").strip()
    
    # Substitui a vírgula por ponto para lidar com números decimais
    views_texto = views_texto.replace(",", ".")
    partes = views_texto.split()
    
    if not partes:
        return 0

    # Tenta converter a primeira parte para float
    try:
        numero = float(partes[0])
    except ValueError:
        print(f"Não foi possível converter '{partes[0]}' para um número.")
        return 0

    # Define o multiplicador baseado na unidade
    multiplicador = 1
    if len(partes) > 1:
        unidade = partes[1]
        if "mil" in unidade:
            multiplicador = 1000
        elif "mi" in unidade or "milhão" in unidade or "milhões" in unidade:
            multiplicador = 1000000
        elif "bi" in unidade or "bilhão" in unidade or "bilhões" in unidade:
            multiplicador = 1000000000

    # Converte para int, multiplicando pelo fator adequado
    try:
        return int(numero * multiplicador)
    except OverflowError:
        print(f"O número é muito grande para ser convertido: {views_texto}")
        return float('inf')
    except Exception as e:
        print(f"Erro ao converter '{views_texto}': {str(e)}")
        return 0

def prepara_query(palavra):
    palavra = palavra.lower().strip().replace(" ","+")
    return palavra


def encontrar_elementos_por_classe(url, nome_classe):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--window-size=1920x1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, nome_classe))
        )
        
        elementos = driver.find_elements(By.CLASS_NAME, nome_classe)
        
        resultados = []
        contador = 0
        
        for elemento in elementos:
            if contador >= 5:
               # driver.quit()
                break
            
            try:
                titulo = elemento.find_element(By.ID, "video-title").text
                meta_block = elemento.find_element(By.ID, "metadata-line")
                views = meta_block.find_element(By.CLASS_NAME, "inline-metadata-item").text
                link = elemento.find_element(By.ID, "video-title").get_attribute("href")
                
                resultados.append({
                    "titulo": titulo,
                    "views": converter_views_para_inteiro(views),
                    "link": link
                })
                
                contador += 1
                    
            except Exception as e:
                print(f"Erro ao extrair informações de um elemento: {e}")
        
        return resultados
    finally:
        driver.quit()
        
        
        
# Código principal
musica = prepara_query("skank ainda gosto dela")
url = f'https://www.youtube.com/results?search_query={musica}'
print(musica)
classe_alvo = "style-scope ytd-video-renderer"

elementos_encontrados = encontrar_elementos_por_classe(url, classe_alvo)

if elementos_encontrados:
    video_mais_visto = max(elementos_encontrados, key=lambda video: video['views'])
    url = video_mais_visto["link"]
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
    driver.refresh()
    #janela_principal.send_keys(Keys.SPACE)
    # Espera para garantir que todas as janelas sejam abertas
    
    # Fecha todas as janelas exceto a principal
    for window_handle in driver.window_handles:
        if window_handle != janela_principal:
            driver.switch_to.window(window_handle)
            driver.close()
    
    # Volta para a janela principal
    driver.switch_to.window(janela_principal)
    
    # Aqui você pode adicionar mais código para interagir com a página do vídeo
    
    input("Pressione Enter para fechar o navegador...")
    driver.quit()
else:
    print("Nenhum vídeo encontrado.")