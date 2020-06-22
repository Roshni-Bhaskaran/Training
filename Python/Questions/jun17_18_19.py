#!/usr/bin/env python
# coding: utf-8

# 1.str= "I am doing well"
#   Find the occurrence of each character in the string

# In[1]:


'''str2 = "I am doing well"
count=0
for i in str2:
    if i=='I' or i=='i':
        count+=1
print(count)'''


# 2.A string contain alphanumeric values and should print only the numeric values present in the string

# In[2]:


def alphanum(str1): 
    s1=[]     
    for i in str1:
        a=i.isnumeric()
        if a==True:
            s1+=i   
    return s1     
            
#alphanum('a7bh89')                


# 4. Print star pattern with 5 rows.

# In[3]:


def star(n):  
    k=n
    for i in range(0, n): 
        for j in range(0, k): 
            print(end=" ") 
        k = k - 1
        for j in range(0, i+1): 
            print("* ", end="") 
        print("\r") 
#n = 5
#star(n) 


# 1.str= "I am doing well" Find the occurrence of each character in the string

# In[4]:


def occurences(t):
    t=t.upper()
    for i in range(len(t)):
        if len(t) == 0:
            break;
        ch = t[0]
        #print(ch)
        if ch == ' ' or ch == '\t':
            continue
        print('The occurrence of '+ch + " - ", t.count(ch))
        t = t.replace(ch, '').strip()
        #print(t)


#occurences('I am doing well') 


# Find length of substring which is not a vowel.

# In[5]:


def long(words):
    for i in "aeiou":
        words = words.lower().replace(i, " ")
        #print(words)
    words = words.split(" ")
    longest = [words[0]]
    for w in words:
        if len(w) > len(longest[0]):
            longest.clear()
            longest.append(w)
            #print(longest)
    #print("Output: " + str(longest))
    return str(longest)
#string = input("Enter the string: ")
#long(string)


# exercise 18/06/20

# Check number palindrome; eg str="121" is a palinrome no but str="-121" is not palindrome
# 

# In[6]:


def palindrome(n):
    t=n
    rev=0
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
        #print(n)
    if(t==rev):
        return 'Palindrome'
    else:
        return "Not a Palindrome"
#n=int(input("Enter number:"))    
#pali=palindrome(n)
#print(pali)


# str=five means output should be 5,4,3,2,1 , one but if str="six" then 6,4,2 ie, 
# odd means all nos less than that no but even means all even nos less than the no (Numeric value must be displayed)



#import wordtodigits
def odd_even(di):
    #print(type(di))
    if di % 2==0:
        #print(di)
        for i in range(di,0,-1):
            if i%2==0:
                print(i)
    else:
        for i in range(di,0,-1):
            print(i)

#ss=input()
#di=wordtodigits.convert(ss)
#odd_even(int(di))


# Q4) accept 2 strings, concatinate the binary string and convert to numeric value, eg:s1="01", s2="10" the output should be : 6

def binaryToDecimal(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    #print(decimal)
    return decimal 

#s1='01'
#s2='10'
#s3=s1+s2
#s3=int(s3)
#binaryToDecimal(s3)


# accept date and what operation must be performed on the date, then from 1970 
# how many years, days, hours, minutes and seconds to this date , calculate and print the ans of operation the user wants to perform
# User can enter 'y' to calc no of years, d to calculate no of days, m for months, min for minutes, s for seconds
# 

# In[37]:


from datetime import datetime
from dateutil import relativedelta
def dates(date_1,date_2,i):
        difference = relativedelta.relativedelta(date_2, date_1)
        months=delta.years*12
        days=delta.years*365
        hours=days*24
        minutes=hours*60
        seconds=minutes*60
        if i=='y':
            print(difference.years)
        elif i=='m':
            months=delta.years*12+delta.months
            print(months)
        elif i=='d':
            print(days)
        elif i=='h':    
            print(hours)
        elif i=='min':
            print(minutes)
        elif i=='s':
            print(seconds)
#date_1 = datetime(1970,1,1,12,0,0)
#date_2 = datetime(2000, 12, 5, 5, 20)
#i=input('y for years,m for month,d for days,h for hours,min for minutes,s for seconds ')
#dates(date_1,date_2,i)


# solutions 19/06/2020
# 

#  Input str and output should be the number of vowels in each word and in a sorted order
# Example:
# Str1="I am Waiting"
# Output:
# I-1
# Am-1
# Waiting-3

# In[41]:


def vowel(string):
    st=[]
    dic={}
    stri=string.lower()
    st=stri.split(' ')
    #print(st)
    for i in st:
        count=0
        for j in i:
            if j in ['a','e','i','o','u']:
                count+=1
                dic[i]=count
    for k in sorted(dic,key=dic.get):
         return (k,dic[k])
#string='I am waiting'
#vowel(string)


#  2X2 Matrix addition and multiplication
#        3X3 Matrix addition and multiplication

# In[49]:
#class threematrix():
def mul(x,y):
    result=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j]+=x[i][k]*y[k][j]
    return result
def add(x,y):
    result=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j]=x[i][j]+y[i][j]
    return result
#x=[[12,7,3],[4,5,6],[7,8,9]]
#y=[[11,5,6],[5,6,9],[2,9,6]]
#ob=threematrix()
#ob.mul(x,y)
#ob.add(x,y)


# In[58]:

#class twomatrix():
def add_matrix(a,b):
    res=[[0,0],[0,0]]
    for i in range(len(a)):
        for j in range(len(a[0])):
            res[i][j]=a[i][j]+b[i][j]
    return res  
def mul_matrix(a,b):
    res=[[0,0],[0,0]]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j]+=a[i][k]*b[k][j]
    return res            
#a=[[1,2],[4,5]]
#b=[[7,8],[10,11]]
#o=twomatrix()
#o.add_matrix(a,b)
#o.mul_matrix(a,b)


# In[ ]:




