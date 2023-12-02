#!/usr/bin/env python
# coding: utf-8

# ## filtering 

# In[3]:


import numpy as np


# In[5]:


arr = np.array([1,2,3,4,5,6,7,8])
x = [True,False,True,False,True,False,True,False]
newarr = arr[x]
print(newarr)


# In[6]:


arr = np.array(['wahid','ali','wazir','beautiful'])
x = [True,False,True,False]
newarr = arr[x]
print(newarr)


# ## create a filter array 

# In[8]:


#Create a filter array that will return only values higher than 42:

import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]


print(newarr)


# In[9]:


arr = np.array([10,20,30,40,50,60,70,80,90,100])
# creating new array list 
newarr = []
# go through each element 
for element in arr:
    if element < 50:
        newarr.append(True)
    else:
        newarr.append(False)

filter_arr = arr[newarr]
print(filter_arr)


# In[10]:


arr = np.array([1,2,3,4,5,6,7,8,9,10])
wahid= []
for element in arr:
    if element < 4:
        wahid.append(False)
    else:
        wahid.append(True)

filter_arr = arr[wahid]
print(filter_arr)


# In[12]:


arr = np.array([11,22,33,44,55,66,77,88])
filtera= []
for element in arr:
    if element % 2== 0:
        filtera.append(True)
    else:
        filtera.append(False)

wahid = arr[filtera]
print(wahid)


# ## generate a random random number from 0 to 100

# In[ ]:




