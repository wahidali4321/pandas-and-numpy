#!/usr/bin/env python
# coding: utf-8

# ## <center> numpy difference

# In[1]:


# a discrete subtracting mean subtract two sucessive array
import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)

print(newarr)


# In[2]:


arr = np.array([10,11,12,13,14,15])
newarr = np.diff(arr)
print(newarr)


# In[3]:


arr = np.array([11,22,33,44,55,66])
newarr = np.diff(arr)
print(newarr)


# In[4]:


# Compute discrete difference of the following array twice:

arr = np.array([11,22,33,44,55])
newarr = np.diff(arr,2)
print(newarr)


# ## finding lcm

# In[5]:


#Find the LCM of the following two numbers:
list1 = [1,2,3,4]
list2 = [5,6,7,8]
x = np.lcm(list1,list2)
print(x)


# In[6]:


li = [22,33,44,55]
lis = [333,44,55,66]
x = np.lcm(li,lis)
print(x)


# In[8]:


# now try on it on another way
la = [11,22,333]
la1 =[221,333,444]
x = np.lcm(la,la1)
print(x)


# In[9]:


#Find the LCM of the values of the following array:
arr = np.array([11,22,33])
x = np.lcm.reduce(arr)
print(x)


# In[10]:


# find the lcm of the values of the following array
arr = np.array([11,22,33,44,55])
x = np.lcm.reduce(arr)
print(x)


# In[11]:


# when we talked about range
arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x)


# In[12]:


import numpy as np

base = 3
perp = 4

x = np.hypot(base, perp)

print(x)


# In[ ]:




