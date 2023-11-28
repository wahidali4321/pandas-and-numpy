#!/usr/bin/env python
# coding: utf-8

# In[2]:


arr = np.array([1,2,3,4,5,6])
print(arr)
print(type(arr))


# # using array as a tuple

# In[3]:


arr = np.array((1,2,3,4,5,6))
print(arr)


# # o- D array

# In[4]:


arr = np.array(42)
print(arr)


# # 1 _ D array
# 

# In[5]:


arr = np.array([1,2,33,44,555])
print(arr)


# # 2- D array
# 

# In[7]:


arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr)


# # 3D array

# In[11]:


arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)


# # to check out whether the dimension is 0,1,2,3

# In[12]:


import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# In[13]:


import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)


# In[15]:


arr = np.array([1,2,3,4], ndmin = 5)
print(arr)
print('number of dimension :', arr.ndim)


# In[ ]:




