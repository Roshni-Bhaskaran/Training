#!/usr/bin/env python
# coding: utf-8

# In[3]:


Fname = 'Roshni'
Lname = 'Bhaskaran'
print("My First name is "+Fname+" and Last name is "+Lname )


# In[6]:


dir(list)


# In[9]:


dir(dict)


# In[10]:


dir(str)


# In[2]:


r='helloworld'


# In[2]:


r.capitalize()


# In[3]:


r.upper()


# In[4]:


r.lower()


# In[19]:


r.count('o')


# In[8]:


r.find("o")


# In[9]:


r.isalnum()


# In[10]:


r.isalpha()


# In[11]:


r.islower()


# In[12]:


r.isupper()


# In[13]:


r.isascii()


# In[14]:


r.isdigit()


# In[15]:


len(r)


# In[16]:


max(r)


# In[17]:


min(r)


# In[18]:


r.swapcase()


# In[20]:


#list
list=[1,2,3,4]


# In[21]:


list1=[1,'a','hello',2]


# In[22]:


list.append(5)


# In[23]:


list


# In[24]:


list.reverse()


# In[25]:


list


# In[26]:


list.sort()


# In[27]:


list


# In[28]:


list.count(1)


# In[29]:


list.extend([6,7])


# In[30]:


list


# In[31]:


list.insert(2,'insert')


# In[32]:


list


# In[33]:


list.remove('insert')


# In[34]:


list


# In[35]:


list.pop(3)


# In[36]:


list


# In[3]:


r[::-1]


# In[4]:


r


# In[5]:


m=['a','e','i']


# In[6]:


m


# In[10]:


m.extend(['o','u'])


# m

# In[11]:


m


# In[7]:


a=0
if a==0:
    print("a is zero")
elif a>0:
    print("a is postive")
elif a<0:
    print("a is negative")


# In[13]:


a1= int(input("enter the integer"))
b1= int(input("enter the integer"))
print(type(a1))
print(type(b1))
if a1>b1:
    print(str(a1)+' is greater')
else:
    print(str(b1)+' is greater')


# 

# In[15]:


name="Roshni Bhaskaran"
for i in name:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        print(' it is a vowel')
    else:
        print("not a vowel")
        
     


# In[ ]:




