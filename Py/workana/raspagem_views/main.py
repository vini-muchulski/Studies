from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://www.facebook.com/cliccamaqua/videos'

# Use o navegador que você quiser
driver = webdriver.Chrome()  # Substitua por Firefox, Edge, etc., se necessário

driver.get(url)
# Ajuste o tempo de espera conforme necessário
wait = WebDriverWait(driver, 10)  # Espera até 10 segundos para que a página carregue

# Ajuste o seletor CSS para encontrar as divs de vídeo, se necessário
videos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.x1n2onr6')))

for video in videos:
    try:
        # Encontra o link do vídeo
        link_element = video.find_element(By.XPATH, './/a[contains(@href, "videos")]')
        link = link_element.get_attribute('href')

        # Encontra o título do vídeo (pode estar em diferentes tags, testando algumas opções)
        try:
            title = video.find_element(By.XPATH, './/span[@dir="auto"]/span').text
        except:
            try:
                title = video.find_element(By.XPATH, './/span[@dir="auto"]').text
            except:
                title = "Título não encontrado"

        # Encontra as visualizações do vídeo
        views_element = video.find_element(By.XPATH, './/span[contains(text(), "views")]')
        views = views_element.text.split()[0]

        print(f"Título: {title}")
        print(f"Link: {link}")
        print(f"Visualizações: {views}")
        print("-" * 20)

    except Exception as e:
        print(f"Erro ao extrair dados do vídeo: {e}")

driver.quit()