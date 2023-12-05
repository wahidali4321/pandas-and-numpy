#!/usr/bin/env python
# coding: utf-8

# # vecterization
# 

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


#example taken from w3 school
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)


# In[11]:


list1 = [1,2,3,4]
list2 = [5,6,7,8]
sumationaa = []


for i , j in zip(list1, list2):
    sumationaa.append(list1+list2)
print(sumationaa)


# In[12]:


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
sumationaa = []

for i, j in zip(list1, list2):
    sumationaa.append(i + j)

print(sumationaa)


# In[13]:


a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = []
for d,e in zip(a,b):
    c.append(d + e)

print(c)


# # task that given me by chat gpt

# In[15]:


list1 =[1,2,3,4]
list2 =[5,6,7,8]
sumationaa = []
for i,j in zip(list1,list2):
    sumationaa.append(i+j)

print(sumationaa)


# In[17]:


# program to perform product and division using zip function
print('the orginal is here')
list1 = [1,2,3,4]
list2 = [5,6,7,8]
print('the list for product')
product =[]
print('the list for division')
division = []
for a,b in zip(list1,list2):
    product.append(a*b)
    division.append(a/b)

print('the product list is here',product)
print('the division list is here',division)


# In[18]:


# program to perform product and division using zip function
print('the original is here')
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

print('\nthe list for product')
product = []
for a, b in zip(list1, list2):
    product.append(a * b)
print('the product list is here', product)

print('\nthe list for division')
division = []
for a, b in zip(list1, list2):
    division.append(a / b)
print('the division list is here', division)


# In[19]:


# Example lists
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

# Using zip to combine lists element-wise
combined = zip(list1, list2)

# Converting the result to a list for display
result_list = list(combined)

# Display the result
print(result_list)


# ## add function is also the same function

# In[20]:


#example of w3 school
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)


# In[21]:


a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = np.add(a,b)
print(c)


# In[23]:


print('the original lists')
a = [11,22,33,44,55]
b = [11,22,33,44,55]
add = np.add(a,b)
print(a)
print(b)
print('the addition of a,b')
print(add)


# In[ ]:




