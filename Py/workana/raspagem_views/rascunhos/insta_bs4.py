import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = "https://www.instagram.com/nasa/reels/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
#print(soup.prettify())

reels = soup.find_all('class', class_='_abq3 _al5p')

print(reels)