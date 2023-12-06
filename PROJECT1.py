#!/usr/bin/env python
# coding: utf-8

# ## <center> import libray

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df = pd.read_csv('amazon.csv')


# In[11]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


# In[7]:


df.info()


# In[12]:


df.describe()


# In[14]:


df['columns'].info()


# In[16]:


df.shape[0]


# In[18]:


df.shape[1]


# In[19]:


df.columns


# In[20]:


df.head()


# In[22]:


df['harddisk'].unique()


# ## <center> observation
#     -- GB
#     -- MB
#     -- TB
#     -- NAN

# In[24]:


df['harddisk'].isnull().sum()


# In[27]:


df['harddisk'].loc[df['harddisk'].str.contains('MB')].value_counts().sum()


# In[ ]:




