
# coding: utf-8

# In[4]:


x = [0.0, 3.0, 5.0, 2.5, 3.7] #define array
print(type(x)) 
#remove 3rd element
x.remove(2.5)
print(x)

#add an element at the end
x.append(1.2)
print(x)

#get a copy
y = x.copy()
print(y)

#show many elements are 0.0
print(y.count(0.0))

#print index with value 3.7

#sort the list
y.sort
print(y)
#reverse sort
y.reverse()
print(y)

#remove all elemts
y.clear()
print(y)

