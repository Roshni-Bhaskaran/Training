#!/usr/bin/env python
# coding: utf-8

# In[5]:


import file2
print(dir(file))


# In[3]:


with open("file.py",'r') as read_obj:
    out=read_obj.readlines()
    for i in out:
        if i.startswith('def'):
            s=i[3:]
            s1=s.split('(')
            print(s1[0])


# In[6]:


with open('file2.py','w') as write_obj:
    write_obj.writelines("Hai this is a string")


# In[7]:


with open('file2.py','a') as append_obj:
    append_obj.writelines(["Hai this is a string\n",'hello\n'])


# In[8]:


f = open("file2.py", "r")
print(f.seek(4))


# In[9]:


f = open("file2.py", "r")
print(f.read())


# In[10]:


f = open("file2.py", "r")
print(f.read(10))


# In[11]:


f = open("file2.py", "r")
print(f.fileno())


# In[12]:


f = open("file.py", "a")
f.write("Now the file has one more line!")
f.flush()
f.write("...and another one!")


# In[13]:


f = open("file2.py", "r")
print(f.isatty())


# In[14]:


f = open("file2.py", "r")
print(f.readable())


# In[15]:


f = open("file2.py", "r")
print(f.readline())


# In[16]:


f = open("file2.py", "r")
print(f.seekable())


# In[17]:


f = open("file2.py", "r")
print(f.tell())


# In[18]:


pip list


# In[2]:


import pandas


# In[3]:


import selenium


# In[4]:


import mysql


# In[5]:


pip install mysql


# In[8]:


import requests


# In[55]:


def get_method(url):
    res=requests.get(url,verify=False)
    if res.status_code in [304,'304',200,'200']:
        return(res.content)
def write_file(filename,data):
    with open(filename,'wb')as w_obj:
        w_obj.write(data)
        return True
    return False
def read_file(filename):
    with open(filename,'r',encoding="utf8")as r_obj:
        out=r_obj.readlines()
        for i in out:
            if i.startswith('<ul><li>') or i.startswith('<li>'):
                sp=i.split('\n')
                f=sp.find('better')
                print(f)
                

            


# In[56]:


data=get_method('https://en.wikipedia.org/wiki/Python_(programming_language)')
status=write_file('wiki.html',data)
file=read_file('wiki.html')
#print(file)
                


# In[57]:


dir(list)


# In[ ]:




