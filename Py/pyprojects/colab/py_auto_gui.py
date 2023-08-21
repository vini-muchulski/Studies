#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pyautogui


# In[3]:


print("ola mundo")


# In[17]:


import pyautogui
import time


# In[30]:


#enviar algo da area de trabalha para o drive

pyautogui.alert("codigo automatizado em processo")
pyautogui.PAUSE= 0.5

#abrir o drive no pc
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("https://drive.google.com/drive/u/0/my-drive")
pyautogui.press("enter")

#ir para area de trabalho
pyautogui.hotkey("winleft","d")
#cliquei no arquivo para fazer backup e arrastar ele
pyautogui.moveTo(342,444)
pyautogui.mouseDown()

pyautogui.moveTo(1353,924)
#enquanto arrastar o arquivo, mudar para o chorme com o drive
pyautogui.hotkey("alt","tab")
#largar o arquivo no drive
time.sleep(1)
pyautogui.mouseUp()
#esperar 5 seg
pyautogui.alert("codigo automatizado em finalizado")
time.sleep(5)




# In[9]:


pyautogui.KEYBOARD_KEYS


# In[29]:


time.sleep(3)
pyautogui.position()


# In[ ]:





# In[ ]:





# In[ ]:




