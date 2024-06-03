
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



driver = webdriver.Chrome()

url = 'https://www.instagram.com/nasa/reels/'

driver.get(url)

time.sleep(5)
videos = driver.find_elements(By.CLASS_NAME,'_ac7v x12nagc xn8zkq8')
print(len(videos))

hrefs = []

for video in videos:



    try:
        # Encontra a tag <a> dentro da div
        anchor = video.find_element(By.TAG_NAME, "a")
        # Extrai o valor do atributo href
        href = anchor.get_attribute("href")
        # Adiciona o href à lista
        hrefs.append(href)
    except:
        # Em caso de erro, passa para o próximo elemento
        print("Erro")
        pass

for href in hrefs:
    print(href)
    
driver.quit()