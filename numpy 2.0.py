#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# # accessing  array element

# In[2]:


arr = np.array([1,2,3,4,5,6])
print(arr[0])


# # get the second element from the array

# In[3]:


arr = np.array(['wahid','ali','wazir','is','belong','to'])
print(arr[1])


# # get the third and fourth , then add both

# In[4]:


arr = np.array([1,2,3,4,5,6,7,8,9,555])
add = arr[2]+arr[3]
print(add)


# # access the 2 D array

# In[11]:


arr = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print('the first row and column',arr[0,1])


# In[12]:


arr = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print('the element of 2nd row and sixth element is : ',arr[1,5])


# # access the third element of first array

# In[28]:


import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[1, 0, 1])


# In[29]:


arr = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12,],[13,14,15,16]]])
print(arr[1, 1,3 ])


# In[31]:


arr = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print('now i want to print the 15 value ? ',arr[1,0,3])


# In[33]:


arr = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(arr[1,0,1])


# In[35]:


arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0,1,-1])


# In[45]:


arr = np.array([[1,2,3,35],[4,5,6,55],[7,8,9,55],[10,11,12,55]])
print(arr[2,3])


# # slicing of element

# In[47]:


arr = np.array([11,22,33,44,55,66,77,88,99])
print(arr[1:4])


# # slicing from element four to end

# In[52]:


arr = np.array([11,22,33,55,66,88,999,999,99999,999])
print(arr[3:])


# import numpy as np

# In[54]:


arr = np.array([11,22,33,44,4444,555])
print(arr[:3])


# In[55]:


arr = np.array([11,22,33,44,4444,555])
print(arr[-3:-1])


# here we uses step 

# In[56]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])


# In[57]:


arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])


# # slicing element from 2 D

# In[58]:


arr = np.array([[1, 2, 3, 4, 5, 6, 7],[1,2,3,4,5,6,7]])
print(arr[1,2:3])


# In[59]:


arr = np.array([10, 15, 20, 25, 30, 35, 40])

print(arr
[::2]
)


# In[ ]:




