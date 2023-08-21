#!/usr/bin/env python
# coding: utf-8

# # bot no computador - pyautogui
# 
# #abrir ferramenta/sistema/arquivo
# #preencher login
# #preencher senha
# #clicar em fazer login

# In[15]:


import pyautogui
import time
pyautogui.PAUSE = 1
#abrir ferramenta
pyautogui.press("winleft")
pyautogui.write("login.xlsx")

pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=3080, y=724)

#preencher login
pyautogui.click(x=2370, y=271)

pyautogui.write("vini")

#preencher senha

pyautogui.click(x=2346, y=316)
pyautogui.write("1234")

#clicar em fazer login
time.sleep(1)
pyautogui.click(x=2398, y=430)


# In[11]:


time.sleep(2)
pyautogui.position()


# In[ ]:


# Point(x=3080, y=724)

#Point(x=2370, y=271)

#Point(x=2346, y=316)

#Point(x=2398, y=430)



# In[ ]:


#bot selenium


# In[22]:


from selenium import webdriver

navegador = webdriver.Chrome()

navegador.get("https://login.live.com/")
#navegador.find_element_by_xpath('//*[@id="i0116"]').send_keys("pythonimpressionador@outlook.com")


# In[ ]:




