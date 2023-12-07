#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import random


# In[2]:


x = random.randint(19)
print(x)


# In[3]:


w = random.randint(11)
print(w)


# In[5]:


w = random.randint(11,low)
print(w)


# In[6]:


z = random.uniform(10)
print(z)


# In[7]:


# we are trying that , else random.randint work on string or not
x = random.randint('z')
print(x)


# In[8]:


# now we try to get random array
x = random.randint(100, size=(4))
print(x)


# In[9]:


x = random.randint(5,size=(5))
print(x)


# In[10]:


x = random.rand(5)

print(x)


# In[11]:


x =random.rand(2)
print(x)


# In[12]:


x = random.uniform(10)
print(x)


# In[13]:


# choice on array
x = random.choice([3, 5, 7, 9])

print(x)


# In[14]:


x = random.choice([11,22,33,44,55])
print(x)


# In[15]:


import numpy as np

# Generate a random integer corresponding to the ASCII value of a character between 'a' and 'z'
random_ascii_value = np.random.randint(ord('a'), ord('z') + 1)

# Convert the ASCII value to the corresponding character
random_character = chr(random_ascii_value)

print("Random character:", random_character)


# In[18]:


random_ascii_value = np.random.randint(ord('a'),ord('z')+1)
random_character = chr(random_ascii_value)
print('random character:', random_character)


# In[20]:


random_ascii_value= np.random.randint(ord('a'),ord('z')+1)
random_character = chr(random_ascii_value)
print(random_character)


# In[21]:


random_ascii_value = np.random.randint(ord('a'),ord('z')+1)
random_char = chr(random_ascii_value)
print(random_char)


# In[22]:


random_ascii = np.random.randint(ord('a'),ord('b')+1)
random = chr(random_ascii)
print(random)


# In[23]:


random_ascii = np.random.randint(ord('a'),ord('b')+1)
ordered = chr(random_ascii)
print(ordered)


# In[24]:


#A random distribution is a set of random numbers that follow a certain probability density function.
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)


# In[25]:


from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)


# In[27]:


from numpy import random
x = random.choice([11,22,33,44], p =[0.1,0.3,0.0,0.6], size=(10))
print(x)


# In[ ]:




