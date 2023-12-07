#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = {'vechical name':['BMW','TESLA','TOYATA','MERCEDES','MG','KIA','ROYAL'],
        'SPEED':[180,125,210,234,333,332,66],
        'COLOR':['RED','GREEN','WHITE','GREY','YELLOW','BLACK','PURPLE'],
        'MADE IN':['JAPAN','AMERICA','CHINA','GERMANY','PAKISTAN','INDIA','south africa'],
        'REVENU':['11 BILLION DOLLAR','7 BILLION DOLLAR','5 BILLION DOLLAR','4 BILLION DOLLAR','3 BILLION DOLLAR','2 BILLION DOLLAR','1 BILLION DOLLAR']}
df = pd.DataFrame(data)
df=pd.DataFrame(df)
df


# In[3]:


def replace_billion_dollar(x):
    if 'BILLION DOLLAR' in str(x):
        return x.replace('BILLION DOLLAR', 'Bn$')
    elif 'MILLION DOLLAR' in str(x):
        return x.replace('MILLION DOLLAR', 'M$')
    else:
        return x

df['REVENU'] = df['REVENU'].apply(replace_billion_dollar)


# In[4]:


def replace_billion_dollar()


# In[ ]:




