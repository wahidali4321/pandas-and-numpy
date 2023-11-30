#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np


# # to check the type of array

# In[10]:


arr= np.array(['wahid','ali','wazir','is','good','boy'])
print(arr.dtype)


# In[11]:


arr = np.array([1,2,3,4,5,6,7])
print(arr.dtype)


# In[12]:


arr = np.array([1.1,2.2,2.2])
print(arr.dtype)


# In[14]:


arr = np.array(['apple', 'banan', 'cherry'])

print(arr.dtype)


# In[16]:


arr = np.array(['apple', 'banan', 'chery'])

print(arr.dtype)


# In[20]:


arr = np.array([1,2,3,4,5],dtype = 'S')
print(arr)
print(arr.dtype)


# In[22]:


arr = np.array([1,2,3,4,5],dtype = 'i')
print(arr)
print(arr.dtype)


# In[23]:


import numpy as np

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)


# In[ ]:




