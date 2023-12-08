#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as df
import numpy as np


# ## series

# a = [1,2,3,4,5,6,7]
# df =pd.Series(a)
# print(df)

# In[9]:


haseeb = [1,2,3,4,5,6,7]
df = pd.Series(haseeb, index = ['a','b','c','d','e','f','g'])
print(df)


# # add and subtract two  series list

# In[15]:


list2 = [1,2,3,4,5]
list1 = [1,2,3,4,5]
list3 = list2 + list1
df = pd.Series(list3)
print(df)


# In[41]:


# subtraction
list2 = [1,2,3,4,5]
list1 = [1,2,3,4,5]
list3 = np.subtract(list2,list1)
print('the orignal data')
print(list3)
print('the series data is ')
df = pd.Series(list3)
print(df)


# In[42]:


list2 = [1,2,3,4,5]
list1 = [1,2,3,4,5]
list3 = np.multiply(list1,list2)
df = pd.Series(list3)
print(df)


# In[38]:


list2 = [1,2,3,4,5]
list1 = [1,2,3,4,5]
list3 = np.add(list1,list2)
print(list3)


# In[44]:


#division
list2 = [1,2,3,4,5]
list1 = [1,2,3,4,5]
list3 =np.divide(list2,list1)
print(list3)
df =pd.Series(list3)
print(df)


# ## QUESTION 5

# In[21]:


data  = { "student":['haseeb','wahid','irfan','umar'],
        "marks":[55,66,77,88],"adddrees":['swabi','wana','mardan','mardan']}
df = pd.DataFrame(data)
print(df)


# #### <center>question 5

# In[23]:


wahid = np.array([1,2,3,3,4,5])
print("the series of the origanl data")
df = pd.Series(wahid)
print(df)


# ### question 6

# In[33]:


data  = { "student":['haseeb','wahid','irfan','umar'],
        "marks":[55,66,77,88],"adddrees":['swabi','wana','mardan','mardan'],'markrs':[333,44,44,55]}
df = pd.DataFrame(data)
print(df)


# In[31]:


color = ['red','blue','orange','red']
df['colors'] = color


# In[30]:


df


# In[32]:


print(df)


# ### here we just need a columns name

# In[35]:


data  = { "student":['haseeb','wahid','irfan','umar'],
        "marks":[55,66,77,88],"adddrees":['swabi','wana','mardan','mardan'],'markrs':[333,44,44,55]}
df = pd.DataFrame(data)
df.columns


# ## index

# In[47]:


data  = { "student":['haseeb','wahid','irfan','umar'],
        "marks":[55,66,77,88],"adddrees":['swabi','wana','mardan','mardan'],'markrs':[333,44,44,55]}
df = pd.DataFrame(data)


# In[49]:


df1=df.set_index('adddrees')


# In[51]:


df1


# In[ ]:


data  = { "student":['haseeb','wahid','irfan','umar'],
        "marks":[55,66,77,88],"adddrees":['swabi','wana','mardan','mardan'],'markrs':[333,44,44,55]}
df = pd.DataFrame(data)


# In[52]:


df2 = df.set_index('student')


# In[53]:


df2


# In[68]:


data  = { "student":['haseeb','wahid','irfan','umar'],
        "marks":[55,66,77,88],"adddrees":['swabi','wana','mardan','mardan'],'markrs':[1,1,1,1],'markrs':[1,1,1,1],'makers':[1,1,1,1]}
df = pd.DataFrame(data)
print(df)


# In[69]:


df.columns


# In[71]:


df.duplicated()


# In[ ]:




