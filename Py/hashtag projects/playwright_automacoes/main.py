from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False) #headless - sem o navegador aparecer
    pagina = navegador.new_page()
    #pagina.goto("https://github.com/vini-muchulski")
    pagina.goto("https://www.hashtagtreinamentos.com/automacao-web-com-playwright-no-python")
    pagina.locator('xpath=//*[@id="s"]').click()
    pagina.fill('xpath=//*[@id="s"]',"python")
    pagina.locator('//*[@id="searchsubmit"]').click()

    time.sleep(5)
    