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
  
url = 'https://www.youtube.com/playlist?list=PLP_dh3S9H39mZwf49qzc1poYv03_hIqzi'
driver = webdriver.Chrome()
driver.get(url)

# style-scope ytd-rich-grid-renderer
# //*[@id="video-title-link"]

# views //*[@id="metadata-line"]/span[1]
#style-scope ytd-rich-grid-renderer
#style-scope ytd-rich-grid-row



videos = driver.find_elements(By.CLASS_NAME,'style-scope ytd-playlist-video-renderer')
#videos = driver.find_elements(By.CLASS_NAME,' style-scope ytd-playlist-video-list-renderer style-scope ytd-playlist-video-list-renderer')
#videos = driver.find_elements(By.CLASS_NAME,'style-scope ytd-item-section-renderer')
#videos = videos.find_element(By.XPATH,'//*[@id="content"]')
for video in videos:
    #title = video.find_element(By.XPATH, './/*[@id="video-title-link"]')
    #views = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text
    content = video.find_element(By.XPATH,'//*[@id="content"]')
    

    #print(content.text)
    titulo = content.find_element(By.XPATH,'//*[@id="video-title"]')

    link = titulo.get_attribute('href')
    print(titulo.text)
    print(link)

    #h3 = content.find_element(By.XPATH,'//*[@id="meta"]/h3')
    #print(h3.get_attribute('aria-label'))

    views = content.find_element(By.XPATH,'//*[@id="video-info"]/span[1]')
    print(views.text)



    #print(f"Title: {title}, Views: {views} Link: {link}")
    

