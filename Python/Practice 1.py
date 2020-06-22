#!/usr/bin/env python
# coding: utf-8

# In[1]:


2+3


# In[2]:


7/4


# In[3]:


7//4


# In[4]:


7%3


# In[5]:


a= 5


# In[6]:


b= 7


# In[7]:


a*b


# In[8]:


salary = 1000


# In[9]:


expenditure = 500


# In[10]:


balance = salary - expenditure


# In[11]:


balance


# In[12]:


type(2)


# In[14]:


type('Rebecca')


# In[15]:


type(10.10)


# In[16]:


'Roshni'


# In[17]:


"Rebecca"


# In[18]:


"I'm a dog"


# In[19]:


print('Hi')
print("Hello")
print("I am Roshni")


# In[20]:


len('Roshni')


# In[21]:


len('Rebecca')


# In[22]:


s = 'Roshni'


# In[23]:


s


# In[31]:


s[-6]


# In[25]:


s[1]


# In[26]:


s[2]


# In[27]:


s[1:]


# In[29]:


s[0:2]


# In[30]:


s[:]


# In[32]:


s[0:6:2]


# In[33]:


s[::-1]


# In[36]:


a = "Hippopotamus is a lazy animal"


# In[37]:


a[::-1]


# In[39]:


'rebecca'*10


# In[40]:


'a'*7


# In[43]:


r = 'Hello Roshni'


# In[44]:


r.upper()


# In[45]:


r.split()


# In[48]:


r.split('n')


# In[53]:


"My dog's name is {}, {} and {}".format('Teddy', 'Jessi', 'Caesar')


# In[1]:


roshni = [21, 'Cse', '7.57']


# In[55]:


len(roshni)


# In[56]:


roshni[0]


# In[57]:


roshni[2]


# In[58]:


roshni[1:]


# In[59]:


roshni[:1]


# In[60]:


roshni[::-1]


# In[61]:


roshni + ['KLU']


# In[62]:


roshni


# In[63]:


roshni = roshni + ['KLU']


# In[64]:


roshni


# In[65]:


roshni += [70.70]


# In[66]:


roshni


# In[67]:


roshni * 2


# In[68]:


roshni


# In[69]:


roshni *=2


# In[70]:


roshni


# In[71]:


roshni.append('R.Patty')


# In[72]:


roshni


# In[74]:


roshni.pop(0)


# In[75]:


roshni


# In[76]:


roshni.pop(3)


# In[77]:


roshni


# In[79]:


roshni.reverse()


# In[80]:


roshni


# In[85]:


new_list = ['Rebecca', 'Teddy', 'Forgia']


# In[86]:


new_list.sort()


# In[87]:


new_list


# In[88]:


lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

a = [lst_1,lst_2,lst_3]


# In[89]:


a


# In[90]:


a[1]


# In[1]:


new_dict = {'name' : 'Rebecca', 'age' : 21}


# In[2]:


new_dict


# In[6]:


new_dict['name']


# In[2]:


d = {'Dog':{'Breed':{'Indian':'Chippiparai', 'Foreign':'German Shephard'}}}


# In[3]:


d['Dog']['Breed']['Foreign']


# In[4]:


d.keys()


# In[19]:


new_dict.keys()


# In[20]:


d.values()


# In[22]:


new_dict.values()


# In[23]:


new_dict.items()


# In[24]:


ab = (1,2,3,4,5)


# In[25]:


len(ab)


# In[38]:


bb = ('Mango', 'apple', 'pineapple', 22, 45, 99, 'Mango')


# In[39]:


bb[0]


# In[40]:


bb[::-1]


# In[41]:


bb[1:]


# In[42]:


bb.index('Mango')


# In[43]:


bb.count('Mango')


# In[46]:


x = set()


# In[47]:


x.add(1)


# In[48]:


x


# In[50]:


x.add(2)


# In[51]:


x


# In[52]:


list1 = [1,2,3,4,5,5,5,6,6,7,7]


# In[53]:


set(list1)


# In[54]:


sample = ['Mango', 'Lemon','Apple', 'Mango']


# In[55]:


set(sample)


# In[56]:


1>100


# In[57]:


2>1


# In[58]:


b = None


# In[61]:


print(b)


# In[63]:


#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

#Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25


# In[64]:


2**6


# In[65]:


2**6/2


# In[66]:


2**6/2*2


# In[67]:


2**6/2*2-4


# In[68]:


2**6/2*2-4+40.25


# In[69]:


s="hello"


# In[70]:


s[1]


# In[71]:


s[::-1]


# In[72]:


s[4]


# In[73]:


s[-1]


# In[74]:


ros=[0,0,0]


# In[75]:


ros


# In[76]:


my=[]


# In[78]:


my.append(0)


# my.append(0)
# 

# In[79]:


my.append(0)


# In[80]:


my.append(0)


# In[81]:


my


# In[95]:


list3 = [1,2,[3,4,'hello']]


# In[101]:


list3[2][2]='goodbye'


# 

# In[102]:


list3


# In[103]:


list4 = [5,3,4,6,1]


# In[104]:


list4.sort()


# In[105]:


list4


# In[106]:


d = {'simple_key':'hello'}


# In[109]:


d['simple_key']


# In[110]:


d = {'k1':{'k2':'hello'}}


# In[112]:


d['k1']['k2']


# In[113]:


d = {'k1':[{'nest_key':['this is deep',['hello']]}]}


# In[123]:


d['k1'][0]['nest_key'][1][0]


# In[124]:


d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}


# In[132]:


d['k1'][2]['k2'][1]['tough'][2][0]


# In[133]:


list5 = [1,2,2,33,4,4,11,22,3,3,2]


# In[134]:


set(list5)


# In[135]:


4**0.5 != 2


# In[136]:


4**0.5


# In[137]:


l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]


# In[138]:


l_one[2][0] >= l_two[2]['k1']


# In[ ]:




