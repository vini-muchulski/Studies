from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extrair_visualizacoes(texto_visualizacoes):
  """
  Extrai o número de visualizações de um texto e o converte para um inteiro.

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
  
url = 'https://www.youtube.com/@RealEngineering/videos'
driver = webdriver.Chrome()
driver.get(url)

# style-scope ytd-rich-grid-renderer
# //*[@id="video-title-link"]

# views //*[@id="metadata-line"]/span[1]
#style-scope ytd-rich-grid-renderer
#style-scope ytd-rich-grid-row



videos = driver.find_elements(By.CLASS_NAME,'style-scope ytd-rich-grid-row')

for video in videos:
    title = video.find_element(By.XPATH, './/*[@id="video-title-link"]')
    views = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text

    link = title.get_attribute('href')
    title = title.get_attribute('title')
    
    views = extrair_visualizacoes(views)

    print(f"Title: {title}, Views: {views} Link: {link}")
    

