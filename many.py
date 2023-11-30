#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyautogui as p
import time

time.sleep(15)

for i in range(10):
    p.typewrite('eee')
    p.press('enter')

