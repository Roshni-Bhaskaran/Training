#!/usr/bin/env python
# coding: utf-8

# In[146]:


stu={'Roshni':{'class':10,'sub':{'maths':80,'science':94,'social':99}},
     'Rebecca':{'class':10,'sub':{'maths':70,'science':69,'social':90}},
     'teddy':{'class':10,'sub':{'maths':89,'science':88,'social':92}},
     'jessi':{'class':10,'sub':{'maths':98,'science':96,'social':100}},
     'ceaser':{'class':10,'sub':{'maths':86,'science':89,'social':95}}}
avg={}
for i,j in stu.items():
    for a,b in j.items():
        if a == 'sub':
            average= (stu[i][a]['maths']+stu[i][a]['science']+stu[i][a]['social'])/3
            avg[i]=round(average)
maximum=max(avg.values())
for c,d in avg.items():
    if maximum==d:
        print('The maximum marks scored by '+c)
            


# In[142]:


avg1=(stu['Roshni']['sub']['maths']+stu['Roshni']['sub']['science']+stu['Roshni']['sub']['social'])/3
avg2=(stu['Rebecca']['sub']['maths']+stu['Rebecca']['sub']['science']+stu['Rebecca']['sub']['social'])/3
avg3=(stu['teddy']['sub']['maths']+stu['teddy']['sub']['science']+stu['teddy']['sub']['social'])/3
avg4=(stu['jessi']['sub']['maths']+stu['jessi']['sub']['science']+stu['jessi']['sub']['social'])/3
avg5=(stu['ceaser']['sub']['maths']+stu['ceaser']['sub']['science']+stu['ceaser']['sub']['social'])/3
print(avg1,avg2,avg3,avg4,avg5)
                
                


# In[2]:


def name(a,b):
    print("My First name is "+a+" and Last name is "+b )
    
Fname = 'Roshni'
Lname = 'Bhaskaran'
name(Fname,Lname)


# In[4]:


def name(Fname,Lname):
    print('first name ',Fname)
    print('last name', Lname)
    print("My First name is "+Fname+" and Last name is "+Lname )
name(Lname='Bhaskaran',Fname='Roshni')


# In[10]:


def check_vowels(name,vowel=['a','e','i','o','u']):
    for i in name:
        if i in vowel:
            print(i)
name="Roshni Bhaskaran"
check_vowels(name)


# In[12]:


def mul_table(num):
    for i in range(1,11):
        print(num*i)
mul_table(num=7)


# In[ ]:




