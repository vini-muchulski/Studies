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
#print(videos)

for video in videos:
    # Ajuste o XPath para encontrar o elemento de visualizações, se necessário
    try:
        
        views = video.find_element(By.XPATH, './/span[1]/div[3]/div/div[2]/span/div/div/span')
        print(views.text) 

        #link = video.find_element(By.XPATH,'//*[@id="mount_0_0_Yx"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div[2]/div[2]/div/div[3]/div/div/div/ul/li[5]/div/div/div/div[2]/span[1]/div[2]/a')
        #print(link.get_attribute('href'))
            
                      
    except:
        pass

driver.quit() 