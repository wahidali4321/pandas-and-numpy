#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import matplotlib.pyplot as plt


# In[14]:


mydataset = {
    "UET":['uet peshware','uet jalozai', "uet mardan", "uet kohat", "uet bannu","uet abbotabod"],
    "no of ranking":[1,2,3,5j,5,6],'no of student ':[2000,1500,1200,1000,1000,300],"rate of job":["22%","55%","60%","40%","40%","99%"],
}
wahid = pd.DataFrame(mydataset,index = ['a','b','c','d','e','f'])
print(wahid)


# In[13]:


wahid.duplicated()


# In[15]:


wahid.corr()


# In[25]:


wahid.plot(kind = 'scatter', x = 'no of ranking', y = 'no of student')
print(wahid)


# In[31]:


wahid.plot(kind = 'scatter', x = 'no of ranking', y = 'no of student')
plt.show()


# In[ ]:




