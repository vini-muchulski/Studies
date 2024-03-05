"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.web import WebBot, Browser
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(WebBot):
    def action(self, execution=None):
      

        # Configure whether or not to run on headless mode
        self.headless = False

      

        # Uncomment to set the WebDriver path
        self.driver_path = "./chromedriver.exe"

    

        # Opens the BotCity website.
        self.browse("https://www.google.com.br/")
        
        if not self.find( "cliquee", matching=0.97, waiting_time=10000):
            self.not_found("cliquee")
        self.click()
        
        self.paste("cotacao dolar")
        self.enter()
              
        if not self.find( "texto_dolar", matching=0.97, waiting_time=10000):
            self.not_found("texto_dolar")
        self.double_click_relative(39, 59)
        
        self.control_c()
        
        cotacao = self.get_clipboard()
        print(cotacao)
        
  

        # Wait for 10 seconds before closing
        self.wait(10000)

        # Stop the browser and clean up
        self.stop_browser()

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()










