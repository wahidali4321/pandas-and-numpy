#!/usr/bin/env python
# coding: utf-8

# ## user_defined function

# In[2]:


def write():
    print('wahid ali')

write()
write()
write()
write()


# In[10]:


# sumation of two numbers using function
def sum(a,b):
    print('the sumation of a and b is :')
    a = 33
    b = 33
    return a+b

result = sum(22,22)
print(result)

d =sum(3,33)
print(d)
e = sum(44,44)
print(e)


# In[21]:


# second function example
def sumation(a,b):
    return a+b
result1 =sumation(11,22)
print(result1)

# another sumation order
a = 44
b = 55
result2=sumation(a,b)
print(result2)
# another sumation order
d = 33
e = 44
result3 = sumation(d,e)
print(result3)


# In[25]:


#here is third one example
def subtraction(a,b):
    return a-b
result1 =subtraction(222,222)
print(result1)
c = 33
d = 33
result =subtraction(c,d)
print(result)


# ## numpy functions

# In[26]:


import numpy as np

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))


# In[29]:


def myadd(x, y):
    return x + y

myadd = np.frompyfunc(myadd, 2,1)
print(myadd([1,2,3,4],[1,2,3,4]))


# In[30]:


def myadd(x, y):
    return x + y

myadd =np.frompyfunc(myadd,2,1)
print(myadd([1,2,3,4],[5,6,7,8]))


# ### here now i'm doing subtraction of the above

# In[34]:


def mysub(x,y):
    return x - y
mysub = np.frompyfunc(mysub,2,1)
print(mysub([1,2],[5,6]))


# ## check if a function is ufunc

# In[38]:


def myadd(x,y):
    return x + y
myadd = np.frompyfunc(myadd,2,1)
print(myadd([1,2,3,4],[1,2,3,4]))
print(np.add)


# In[45]:


# now we check for subtraction
def mysub(x,y):
    return x -y
    
mysub = np.frompyfunc(mysub,2,1)
print(mysub([1,2,3,4],[1,2,3,4]))
print(np.add)


# ## use if statement to check the statement is ufunc or not

# In[46]:


if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')


# In[47]:


def mysub(x,y):
    return x -y
    
mysub = np.frompyfunc(mysub,2,1)
print(mysub([1,2,3,4],[1,2,3,4]))
if type(np.add) == np.ufunc:
    print('add is ufunc')
else:
    print('add is not ufunc')


# In[48]:


if type(np.add) == np.ufunc:
    print('addd is ufunc')
else:
    print('add is not ufunc')


# ### simple arthimatic

# In[49]:


#The add() function sums the content of two arrays, and return the results in a new array.
a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,4,5,6,7,8,9]

add = np.add(a,b)
print('the addition of a and b is :',add)


# In[50]:


#The add() function sums the content of two arrays, and return the results in a new array.
wah = [11,22,33,44]
ali = [11,22,33,44]
print('the original array is ')
print(wah)
print(ali)
#the addition of these two is we install this in 
myadd = np.add(wah,ali)
print('the addition of wah and ali is :',myadd)


# ## subtraction

# In[53]:


#The subtract() function subtracts the values from one array with the values from another array, and return the results in a new arra
ali = [11,22,33,44]
wah = [22,33,44,55]
sub = np.subtract(ali,wah)
print(sub)



# In[54]:


a = [11,22,33,44,55]
b = [11,22,33,44,55]
sub = np.subtract(a,b)
print(sub)


# ## multiplying

# In[60]:


a = [1,2,3,4,5,6]
b = [22,33,44,11,2,3]
mul = np.multiply(a,b)
print('the result is given below')
print(mul)


# ## division

# In[61]:


a = [11,22,33,44,55]
b = [11,22,33,44,55]
division = np.divide(a,b)
print(division)


# ## power

# In[62]:


arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])

newarr = np.power(arr1, arr2)

print(newarr)


# ## Truncation

# In[63]:


# Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
arr = np.trunc([-3.1666, 3.6667])

print(arr)


# In[64]:


arr = np.trunc([22.2,3.99])
print(arr)


# In[65]:


arr = np.trunc([22.1,3.22])
print(arr)


# ## using fix function

# In[66]:


arr = np.fix([-3.1666, 3.6667])

print(arr)


# ## numpy log

# In[67]:


#Find log at base 2 of all elements of following array:
arr = np.arange(1,10)
print(np.log2(arr))


# In[68]:


arr = np.arange(1,10)
print(np.log2(arr))


# In[69]:


arr = np.arange(1,10)
print(np.log2(arr))


# In[70]:


arr = np.arange(1,12)
print(np.log2(arr))


# ## log at base 10

# In[71]:


arr = np.arange(1,5)
print(np.log10(arr))


# ### numpy sumation 

# ##### difference between summation and addition is  addition is done between two argument and summation is done over n number

# In[72]:


arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)

print(newarr)


# In[73]:


ali = np.array([1,2,3,4,5,6])
wah = np.array([1,2,3,4,5,6])
wahidali = np.add(ali,wah)
print(wahidali)


# In[77]:


# sumatioin
ali = np.array([1,2,3,4,5,6])
wah = np.array([1,2,3,4,5,6])
wahidali = np.sum([ali,wah])
print(wahidali)


# In[76]:


import numpy as np

ali = np.array([1, 2, 3, 4, 5, 6])
wah = np.array([1, 2, 3, 4, 5, 6])
wahidali = np.sum([ali, wah])
print(wahidali)


# In[80]:


arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])


newarr = np.sum([arr1, arr2], axis=1)

print(newarr)


# In[83]:


arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3])
arr3 = np.array([1,2,3])
arr4 = np.array([1,2,3])
suma = np.sum([arr1,arr2,arr3,arr4], axis = 2)
print(suma)


# In[85]:


import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
arr3 = np.array([1, 2, 3])
arr4 = np.array([1, 2, 3])

# Use axis=0 or axis=None for 1-dimensional arrays
suma = np.sum([arr1, arr2, arr3, arr4], axis=1)
print(suma)


# ## cumulative addition

# In[86]:


import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
arr3 = np.array([1, 2, 3])
arr4 = np.array([1, 2, 3])

# Use axis=0 or axis=None for 1-dimensional arrays
suma = np.sum([arr1, arr2, arr3, arr4], axis=0)
print(suma)


# In[87]:


arr = np.array([1, 2, 3])

newarr = np.cumsum(arr)

print(newarr)


# In[ ]:




