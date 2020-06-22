#!/usr/bin/env python
# coding: utf-8

# In[9]:


list1=[1,2,3,'hai','hello',3.1,4.8,'Roshni',33,99.9]
integer=[]
string=[]
f=[]
for i in list1:
    if type(i)== int:
        integer.append(i)
    elif type(i)== str:
        string.append(i)
    else:
        f.append(i)
print(integer)
print(string)
print(f)


# In[2]:


num =7
for i in range(1,11):
    print(num*i)


# In[10]:


list2=[-4,3,1,6,-7,0,-9,-1,5]
pos_count=0
neg_count1=0
for i in list2:
    if i>=0:
        pos_count+=1
    else:
        neg_count1+=1
print('Positive number count '+str(count))
print('negative number count '+str(count1))
        


# In[8]:


cube=0
while(1):
    number=input('Enter the number or q to quit ')
    if number=='q':
        break
    else:
        cube=int(number)*int(number)*int(number)
        print('The cube of number '+str(number)+' is '+str(cube))


# In[2]:


m={'stud1': {'name': 'student1', 'marks': [99, 44, 88]}, 'stud2': {'name': 'student2', 'marks': [88, 66, 88]}}


# In[3]:


for i, j in m.items():
       for a,b in j.items():
           if a == 'marks':
               print("Totak marks scored by - "+i+" is "+str(sum(b)))


# In[3]:


m['stud1']['marks'][1]


# In[4]:


sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}


# In[6]:


sampleDict['emp4']={'name':'Smith', 'salary':15000}


# In[9]:


sampleDict


# In[8]:


sampleDict['emp2']['salary']=10000


# In[13]:


for i,j in sampleDict.items():
    for a,b in j.items():
        print(i,a,b)


# In[ ]:




