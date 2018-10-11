
# coding: utf-8

# In[ ]:


#check_in_solution.py

#include the numpy library
import numpy as np
#defining main function

def main():
    i = 0 #declaring integer
    x = 119.0 #declaring float
    for i in range(120) # loop i from 0 to 119
        if((i%2)==0): # if i is even
            x += 3. #add 3 to x
        else:
            x -= 5. #subtract 5 from x
    s = "%3.2e" % x #string containing x in sci notation
    print(s)

#rest of program continues
if_name_=="_main": #if main() exists, then run it
    main()

