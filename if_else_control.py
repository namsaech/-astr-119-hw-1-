
# coding: utf-8

# In[1]:


#if else control

#define function
def flow_control(k):
    #define string based on k value
    if(k==0):
        s = "variable k = %d equals 0" % k
    elif(k==1): 
        s = "variable k = %d equals 1" % k
    else:
        s = "variable k = %d does not equal 0 or 1" % k
    # print variable
    print(s)
#define main function
def main():
    i = 0
    
    #try flow control for 0, 1, 2
    flow_control(i)
    i = 1
    flow_control(i)
    i = 2
    flow_control(i)
#run the program
if __name__ == "_main_":
    main()
#error, name is not define in line 25

