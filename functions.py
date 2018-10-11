
# coding: utf-8

# In[5]:


import numpy as np
import sys

#define function that returns value
def expo(x):
    return np.expo(x) #returns e^x function

#define subroutine that does not return value
def show_expo(n):
    for i in range(n):
        print(expo(float(i))) #calls expo function
#define main function
def main():
    n = 10 #default function for n
    
    #check if there is command line argument
    if(len(sys.argv)>1):
            n = int(sys.argv[1]) #If argument provided, use it for n
        
    show_expo(n) #call show_expo subroutine
#runs the main function 
if __name__ == "__main__":
    main()
    
        

