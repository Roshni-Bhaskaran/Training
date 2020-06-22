#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=5
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(col,end='')
    print()    
    


# In[6]:


list1=[]
count=0
count1=0
for i in range(533,875):
    list1.append(i)
for i in list1:
    if i%2==0:
        count+=1
    else:
        count1+=1
print(count)
print(count1)


# In[1]:


credit_no=int(input("Enter the no: of cards: "))
list1=[]
for i in range(0,credit_no):
    no = str(input(""))
    list1.append(no)
for i in list1:
    if i[0][0] in ['4','5','6'] and len(i) == 16:
        #for c in :
            print('valid')
           # if c in ['0','1','2','3','4','5','6','7','8','9']:
    else:
        
        print('invalid')   


# In[12]:


credit_lt = ['4253625879615786','4424424424442444','5122-2368-7954-3214','42536258796157867','4424444424442444','5122-2368-7954 - 3214','44244x4424442444','0525362587961578']
for no in credit_lt:   # iterating the list using for loop
    if no.startswith('4') or no.startswith('5') or no.startswith('6'):
        if ' ' not in no and '_' not in no:
            if len(no) >= 16 and len(no) <=19 and 'x' not in no:
                #print(no)  (1234)-(4567)-(8901)-(1235)
                flag = 0
                if '-' in no:
                    split_val = no.split('-')
                    for i in split_val:
                        if len(i) !=4:
                           flag = 1
                print(no)
                '''
                if flag == 0:
                    skip_flag = 0
                    for j in list(range(10)):
                        #print(no,j)
                        count_val = str(no).count(str(j))
                        if count_val > 4:
                            skip_flag = 1
                            continue
                    if skip_flag ==1:
                        continue
                    print(no)
                '''


# In[ ]:




