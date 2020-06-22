#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Arithmetic():
    def add(self,a,b):
        c=a+b
        return c
    def sub(self,a,b):
        c=a-b
        return c
    def mul(self,a,b):
        c=a*b
        return c
obj=Arithmetic()
#print(dir(obj))
ad=obj.add(2,2)
su=obj.sub(2,2)
mu=obj.mul(2,2)
print(ad)
print(su)
print(mu)


# In[72]:


class string_fun():
    def lower_case(self,s):
        '''This function will convert the string into lower case'''
        try:
            lower=s.lower()
            return lower
        except Exception as e:
            return e
    def upper_case(self,s):
        '''This function will convert the string into upper case'''
        try:
            upper=s.upper()
            return upper
        except Exception as e:
            return e
    def split(self,s):
        '''This function will split the given string'''
        try:
            split=s.split()
            return split
        except Exception as e:
            return e
    def vowels(self,s):
        '''This function will print the vowels present in the string'''
        try:
            v=[]
            for i in s:
                if i in ['a','e','i','o','u']:
                    v.append(i)
            return v
        except Exception as e:
            return e
name="Roshni Bhaskaran"
obj=string_fun()
a=obj.lower_case(name)
b=obj.upper_case(name)
c=obj.split(name)
d=obj.vowels(name)
print(a)
print(b)
print(c)
print(d)


# In[4]:


def is_sorted(lis):
    '''This function will sort the elements in ascending order'''
    try:
        lis1=lis[:]
        lis.sort()
        #print(lis)
        #print(lis1)
        if lis==lis1:
            return False
        else:
            return True
    except Exception as e:
        return e
sor=is_sorted(['u','a','g','y'])    
print(sor)    


# In[8]:


def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print ("The argument does not contain numbers\n", Argument)

temp_convert("xyz");


# In[1]:


pip list


# In[2]:


pip install yaml


# In[ ]:




