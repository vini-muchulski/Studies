from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extrair_visualizacoes(texto_visualizacoes):
  """
  Extrai o número de visualizações de um texto.

  Args:
    texto_visualizacoes: O texto que contém as visualizações, por exemplo,
                         "Views: 676 mil visualizações".

  Returns:
    O número de visualizações como um inteiro, ou None se não for possível extrair.
  """
  partes = texto_visualizacoes.split()
  if 'mil' in partes:
    indice_mil = partes.index('mil')
    try:
      numero_mil = float(partes[indice_mil - 1].replace(',', '.'))
      return int(numero_mil * 1000)
    except ValueError:
      return None
  elif 'mi' in partes:
    indice_mi = partes.index('mi')
    try:
      numero_mi = float(partes[indice_mi - 1].replace(',', '.'))
      return int(numero_mi * 1000000)
    except ValueError:
      return None
  else:
    return None

url = 'https://www.youtube.com/playlist?list=PLP_dh3S9H39mZwf49qzc1poYv03_hIqzi'
driver = webdriver.Chrome()
driver.get(url)

# Aguarda o carregamento dos vídeos da playlist
wait = WebDriverWait(driver, 10)
videos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ytd-playlist-video-renderer')))

for video in videos:
    content = video.find_element(By.ID, 'content')
    titulo = content.find_element(By.ID, 'video-title')
    link = titulo.get_attribute('href')
    print(titulo.text)
    print(link)

    views = content.find_element(By.XPATH, './/*[@id="video-info"]/span[1]')
    visualizacoes = extrair_visualizacoes(views.text)
    print(f"Visualizações: {visualizacoes}")

driver.quit()