
# coding: utf-8

# In[1]:


#exceptions, lets me deal with unexpected results

try:
    print(a) #throw exception cause a is not defined
except:
    print("a is not defined")
#specific errors to help with cases

try:
    print(a)
except NameError:
    print("a is still not defined")
except:
    print("something else went wrong")
#program breaks because a is not defined
print(a)

#ran in jupyter, error says that name 'a" is not defined

