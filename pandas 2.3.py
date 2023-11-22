#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df = pd.read_csv('a.csv')
print(df)


# In[4]:


new_df = df.dropna()
print(new_df.to_string())


# In[5]:


wahid = df.dropna()
print(wahid.to_string())


# In[6]:


df.dropna(inplace= True)
print(df.to_string())


# In[8]:


df.fillna(130 , inplace = True)


# In[ ]:




