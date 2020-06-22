#!/usr/bin/env python
# coding: utf-8

# In[3]:


def Celsius_to_Fahrenheit(c) :
    f = (9/5)*c + 32
    return f
def Fahrenheit_to_Celsius(f) :
    c = (5/9)*(f - 32)
    return c
Fah=Celsius_to_Fahrenheit(55)
Cel=Fahrenheit_to_Celsius(98)
print(Fah)
print(Cel)


# In[15]:


def reverse(s):
    s1 = ''
    for c in s:
        #print(c)
        s1 = c + s1
    return s1

string=reverse('HAIHELLO')
print(string)


# In[ ]:





# In[33]:


def fun(a,b=1):
    try:
        #print(b)
        if b==0:
            raise ValueError;
        else:
            print('b = '+str(b))
    except ValueError:
        print('b = 0')
fun(3,5)        


# In[42]:


def is_abecedarian(a):
    sort=sorted(a)
    b=[]
    for i in a:
        b.append(i)
        #print(org)
    if sort == b:
        return True
    else:
        return False
value=is_abecedarian('Aadil')
print(value)
value1=is_abecedarian('banana')
print(value1)


# In[ ]:




