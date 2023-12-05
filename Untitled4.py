#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[11]:


mydataset = {
    "UET":['uet peshware','uet jalozai', "uet mardan", "uet kohat", "uet bannu","uet abbotabod"],
    "no of ranking":[1,2,3,4,5,6],'no of student ':[2000,1500,1200,1000,500,300],"rate of job":["22%","55%","60%","40%","11%","99%"],
}
wahid = pd.DataFrame(mydataset,index = ['a','b','c','d','e','f'])
print(wahid)


# In[ ]:




