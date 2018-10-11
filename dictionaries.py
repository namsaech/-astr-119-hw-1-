
# coding: utf-8

# In[2]:


#define dictionary data structure

#dictionaries have key: value for the elements
example_dict = {
    "class"  :  "astr 119",
    "prof"   :  "Brant",
    "awesomeness"  : 100
}
print(type(example_dict)) #will print type dict

#get a value via key
example_dict["awesomeness"] += 1 #increase awesomeness

#print dictionary
print(example_dict)

#print dictionary element by element
for x in example_dict.keys():
    print(x, example_dict[x])

