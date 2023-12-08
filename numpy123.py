#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)


# In[4]:


from numpy import random
import numpy as np
arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)


# ## shuffling

# In[12]:


arr = np.array([11,22,33,4,5])
random.shuffle(arr)
print(arr)


# ### permutation

# In[15]:


from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))


# ##<center> seaborn 

# In[16]:


import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()


# In[19]:


from numpy import random
import numpy
data =[0, 1, 2, 3, 4, 5]
datas = numpy.mean(data)
print(datas)


# In[20]:


import matplotlib.pyplot as plt
import seaborn as sns

data = [0, 1, 2, 3, 4, 5]

# Use histplot instead of distplot
sns.histplot(data)

plt.show()


# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()


# In[23]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([11,22,33,44,33,33,33,55,66])
plt.show()


# In[24]:


import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()


# In[ ]:




