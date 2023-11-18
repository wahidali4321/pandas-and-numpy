#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn


# In[8]:


pd.read_csv('amazon.csv')


# In[52]:


df.info()


# In[53]:


df.isnull()


# In[55]:


sns.heatmap(df.isnull())sum(df)


# In[56]:


df['price'].unique()


# In[57]:


df.nunique()


# In[63]:


df.columns


# In[64]:


df['brand'].unique


# In[65]:


df['model'].uniqueque


# In[66]:


df['cpu_speed'].value_counts()


# In[6]:


pd.isnull()


# In[ ]:




