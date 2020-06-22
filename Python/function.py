#!/usr/bin/env python
# coding: utf-8

# In[4]:


def comma_Sep(string):
    ''' This function will get the string and 
    split the string using comma and store it in list and tuple'''
    list1=string.split(',')
    tuple1=tuple(list1)
    print(list1)
    print(tuple1)
    
string=input('Enter the values')
comma_Sep(string)
print(comma_Sep.__doc__)


# In[21]:


def multiple(number):
    '''This function will give the values which is divisible by 7 but not multiple of 5'''
    values=[]
    for i in number:
        #print(i)
        if i%7==0:
            if i%5!=0:
                print(i, end=",")               
number=[]
for i in range(5000,7501):
    number.append(i)
multiple(number)    


# In[24]:


def Fibonacci(n):
    '''This function will generate fibonacci series upto given n values'''
    n1, n2 = 0, 1
    count = 0
    if n<= 0:
        print("Please enter a positive integer")
    elif n == 1:
        #print("Fibonacci sequence upto",nterms,":")
        print(n1)
    else:
        while count < n:
            print(n1,end=",")
            n3 = n1 + n2
            # update values
            n1 = n2
            n2 = n3
            count += 1
        
n = 200
Fibonacci(n)


# In[ ]:




