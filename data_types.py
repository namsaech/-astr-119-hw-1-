
# coding: utf-8

# In[2]:


import numpy as np

i = 10
print(type(i)) #shoul print out int data type
a_i = np.zeros(i,dtype=int) #declare array of int
print(type(a_i)) #returns ndarray
print(type(a_i[0])) #return int64

x = 119.0
print(type(x)) #will return data type float

y = 1.19e2
print(type(y))

z = np.zeros(i,dtype=float)
print(type(z))
print(type(z[0]))

