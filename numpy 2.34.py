#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[6]:


arr = np.array([1, 2, 3])

for x in arr:
  print(x)


# ## random value

# In[10]:


from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)


# In[11]:


x = random.choice([1,2,3,4], p=[0.1,0.3,0.6,0.0], size=(100))
print(x)


# In[13]:


wahid = random.choice([1,2,3,4],p=[0.6,0.2,0.1,0.1], size=(50))
print(wahid)


# ## 2 D array

# In[14]:


#Same example as above, but return a 2-D array with 3 rows, each containing 5 values.
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)


# In[15]:


arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)


# In[16]:


arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)


# In[17]:


arr = np.array([1,2,3,4,5,6,7,8])
random.shuffle(arr)
print(arr)


# ## generation of permutation of array

# In[18]:


#Generate a random permutation of elements of following array
arr = np.array([1,2,3,4,5,6])
print(random.permutation(arr))


# # importing matloplib

# In[19]:


import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()


# In[20]:


import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()


# In[ ]:




