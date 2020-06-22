#!/usr/bin/env python
# coding: utf-8

# In[23]:


def sum_digits(s,num=['0','1','2','3','4','5','6','7','8','9']):
    sum=0
    for i in s:
        if i in num:
            sum=sum+int(i)
    print(sum)

s="a2b3c"
sum_digits(s)


# In[4]:


def palindrome(s):
    rev=s[::-1]
    if s==rev:
        print('True')
    else:
        print('False')
s='madam'
palindrome(s)


# In[29]:


def mul_table(num):
    for i in range(1,11):
        print(num*i)
mul_table(num=7)


# In[31]:


def pattern(n):
    for row in range(n,0,-1):
        for col in range(1,row+1):
            print(col,end='')
        print()  
n=5
pattern(n)


# In[33]:


def count(list1):
    count=0
    count1=0
    for i in list1:
        if i%2==0:
            count+=1
        else:
            count1+=1
    print(count)
    print(count1)
list1=[]
for i in range(533,875):
    list1.append(i)
count(list1)    


# In[35]:


def datatype(list1):
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
list1=[1,2,3,'hai','hello',3.1,4.8,'Roshni',33,99.9]
datatype(list1)


# In[40]:


def posneg(list2):
    pos_count=0
    neg_count1=0
    for i in list2:
        if i>=0:
            pos_count+=1
        else:
            neg_count1+=1
    print('Positive number count '+str(pos_count))
    print('negative number count '+str(neg_count1))
list2=[-4,3,1,6,-7,0,-9,-1,5]
posneg(list2)


# In[41]:


def check_vowels(name,vowel=['a','e','i','o','u']):
    for i in name:
        if i in vowel:
            print(i)
name="Roshni Bhaskaran"
check_vowels(name)


# In[43]:


def find_cube(number):
    cube=0
    cube=int(number)*int(number)*int(number)
    print('The cube of number '+str(number)+' is '+str(cube))
    
while(1):
    number=input('Enter the number or q to quit ')
    if number=='q':
        break
    else:
        find_cube(number)


# In[6]:


def binaryToDecimal(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    print(decimal)     
      
binary=10011
binaryToDecimal(binary)


# In[13]:


def upper_lower(sen):
    upper=0
    lower=0
    for i in sen:
        if i.isupper():
            upper+=1
        else:
            lower+=1
    print(upper)
    print(lower)
sen='RoshniBhaskaran'    
upper_lower(sen)    
            


# In[ ]:





# In[ ]:





# In[ ]:




