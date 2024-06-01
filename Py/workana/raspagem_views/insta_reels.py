from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

url = 'https://www.instagram.com/nasa/reels/'

driver.get(url)

# Aguarda o carregamento dos vídeos da playlist

#videos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1' )))

time.sleep(5)
videos = driver.find_elements(By.CLASS_NAME,'xvbhtw8 x78zum5 xdt5ytf x1iyjqo2 x182iqb8')
""" x9f619 xjbqb8w x78zum5   x168nmei x13lgxp2 x5pf9jr xo71vjh   x1n2onr6 x1plvlek xryxfnj x1c4vz4f   x2lah0s xdt5ytf xqjyukv x1qjc9v5   x1oa3qoh x1nhvcw1"""

#videos = driver.find_elements(By.XPATH,'//*[@id="mount_0_0_mP"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/div[2]/div/div/div[1]/div[1]')
#cada video
#x1qjc9v5 x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 xdt5ytf x2lah0s xln7xf2 xk390pu xdj266r xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x11njtxf xpzaatj xw3qccf

print(videos)   
# numero views
#html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs


#link reels
#x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd



for video in videos:



    link = video.find_element(By.XPATH, '//*[@id="mount_0_0_Ax"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/div[2]/div/div/div[1]/div[1]/div/a')
    link = link.get_attribute('href')

    print(link)


driver.quit()