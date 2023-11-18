#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#    reading the data
import pandas as pd
df=pd.read_csv('a.csv')
print(df)


# In[3]:


# information about the data
df.info()


# In[4]:


# to find out the null value 
df.isnull()


# In[5]:


# to find out the sum of null value
df.isnull().sum()


# In[6]:


# to find out the percentage of null value 
df.isnull().sum()/len(df)*100


# In[ ]:


## to show just one column
df['Population 2020']


# In[9]:


df['Migrants (net)']


# In[10]:


#to find out mean value
df['Migrants (net)'].count


# In[13]:


df['Migrants (net)'].mean


# In[15]:


df['Migrants (net)'].min


# In[ ]:




