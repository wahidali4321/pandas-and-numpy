#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)


# In[3]:


import pandas as pd
mydataset = {'CARS' : ['BMW', 'TOTOYA', 'MERCEDES'], 'PASSING' : [1, 2, 3]}
myvar = pd.DataFrame(mydataset)
print(myvar)


# In[7]:


import pandas as pd
myDataset = {'CARS ': ['BMW','TOYATA','MERCEDES'], "PASSING" : [1, 2, 3]}
var = pd.DataFrame(myDataset)
print(var)


# In[10]:


import pandas as pd
Data = {'CARS': ['MERCEDES','TOYOTA','TESLA'], 'PRICES' : [333,4444,5555]}
var = pd.DataFrame(Data)
print(var)


# In[13]:


import pandas as pd
Data = {'Departement':['computer science', 'mechanical engineering','civil engineering','electrical engineering'],'rank':[444,555,66,77]}
var = pd.DataFrame(Data)
print(var)


# In[14]:


Data = {'Department':['computer science','electrical engineering','mechanical engineering','data science'],'rank':[22,33,44,55]}
var = pd.DataFrame(Data)
print(var)


# In[15]:


import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)


# In[17]:


import pandas as pd
a = [1, 7, 4]
var = pd.Series(a)
print(var)


# In[18]:


import pandas as pd
a  = [11, 22, 33, 44]
var = pd.Series(a)
print(var)


# In[19]:


Data = [22, 33, 55, 77, 99]
var = pd.Series(Data)
print(Data[3])


# In[ ]:




