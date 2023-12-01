#!/usr/bin/env python
# coding: utf-8

# # converting  datatype on existing array
# 

# In[1]:


import numpy as np


# In[2]:


arr = np.array([1.2,2.3,3.4,4.5])
newarr = arr.astype('i')
print(newarr)
print(newarr.astype)


# In[3]:


arr = np.array([1.2,2.3,3.4,4.5])
newarr = arr.astype(int)
print(newarr)
print(newarr.astype)


# # converting int into float

# In[4]:


arr = np.array([1,2,3,4,5,6,7,8])
new = arr.astype('f')
print(new)
print(new.astype)


# # converting int into string

# In[5]:


arr = np.array([1,2,3,4,5,6,7,8,8])
nw = arr.astype('S')
print(nw)
print(nw.astype)


# # converting string into boolen

# In[9]:


arr = np.array(['wahid','ali','wazir'])
nw= arr.astype(bool)
print(nw.dtype)


# # converting int into bool

# In[11]:


arr = np.array([1,2,3,4,5,6])
nw = arr.astype(bool)
print(nw)
print(nw.dtype)


# In[8]:


import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)


# # the difference between copy vs original

# ### make a copy change the original array, and display both array

# In[12]:


arr = np.array([1,2,3,4,5,6,7])
nw = arr.copy()
arr[0]= 42
print(nw)
print(arr)


# In[13]:


arr = np.array([1,2,3,4,5,6,7,8])
new = arr.copy()
arr[0]= 33
print(arr)
print(new)


# In[16]:


arr = np.array([1,2,3,4,5,6,7])
nw = arr.copy()
arr[::3]= 42
print(nw)
print(arr)


# In[17]:


arr = np.array([1,2,3,4,5,6,7])
nw = arr.copy()
arr[0:3]= 42
print(nw)
print(arr)


# ## make a view change the original and display both

# In[19]:


arr = np.array([11,22,33,44,55,66,77,88,99])
nw = arr.view()
nw[1:3]= 0
print(arr)
print(nw)


# In[20]:


arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)


# ## make change in the view

# In[21]:


arr = np.array([1,2,3,4,5,6,7,8])
nw = arr.copy()
nw[1:2] = 22
print(arr)
print(nw)


# ### make change in the copy

# In[25]:


arr = np.array([1,2,3,4,5,6,7,8])
nw = arr.copy()
nw[1:2]= 22
print(nw)
print(arr)


# # check if array owns data

# In[26]:


arr= np.array([1,2,3,4,5,6,7])
cop = arr.copy()
view = arr.view()
print(cop.base)
print(view.base)


# In[27]:


arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)


# ### shape  of an array

# In[37]:


arr = np.array([[1,2,3,4,6],[5,6,7,8,7]])
print(arr.shape)


# In[38]:


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)


# In[39]:


arr = np.array([1,2,3,4,5], ndmin=5)
print(arr)
print('shape of array :',arr.shape)


# # reshape from one D to two D

# In[40]:


arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)
print(newarr)


# In[47]:


student = np.array(['Name','class','registration number','regional area','wahid','2nd year','22pwdsc0054','waziristan','abu baker','2nd year','22pwdsc0053','waziristan'])
nw = student.reshape(4,3)
print(nw)


# ## reshape 1D to 3D

# In[48]:


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)


# In[49]:


arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)


# # iterating element

# In[50]:


arr = np.array([1,2,3,4,5,6,7,8])
for x in  arr:
    print(x)


# In[51]:


arr = np.array([1,2,3,4,5,6,7,8,9,11,111,22])
for x in arr:
    print(x)


# In[52]:


arr = np.array([11,22,33,44,55,66,77,88])
for x in arr:
    print(x)


# In[53]:


arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for x in arr:
    print(x)


# In[54]:


arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)


# 

# # joing two array

# In[57]:


arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
arr = np.concatenate((arr1 , arr2))
print(arr)


# In[58]:


arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
arr = np.concatenate((arr1,arr2))
print(arr)


# In[66]:


arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)

print(arr)


# # array  spliting

# In[67]:


arr = np.array([1,2,3,4,5,6,7,8])
new = np.array_split(arr,3)
print(new)


# In[68]:


arr = np.array([11,22,33,44,55,66,77,88,99,00,1111,2222,3333])
new = np.array_split(arr, 2)
print(new)


# In[72]:


arr = np.array([11,22,33,44,55,66,7777,888,999,0000])
new_arr = np.array_split(arr,5)
print(new_arr[0])
print(new_arr[1])
print(new_arr[2])


# # searching array

# In[74]:


arr =np.array ([1,2,3,4,5,6,7,8,9])
new = np.where(arr==3)
print(new)


# In[75]:


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)


# In[76]:


arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)


# In[77]:


arr = np.array([6,7,8,9])
new = np.searchsorted(arr,7)
print(new)


# # sorting the data

# In[80]:


arr = np.array([33,2,3,44,5,6,7,8,9])
new = np.sort(arr)
print(new)


# In[84]:


arr = np.array(['bzanana', 'bherry', 'cpple'])

print(np.sort(arr))


# In[ ]:




