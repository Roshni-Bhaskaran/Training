#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x
    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y
    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    def eq(self):
        if self.x==self.y:
            return True
        else:
            return False
    def repr(self):
        express='self.x*self.x+55+self.y-10'
        y=eval(express)
        return y
        
obj=Coordinate(55,56)
print(obj.x)
print(obj.y)
a=obj.__str__()
print(a)
b=obj.repr()
print(b)
c=obj.eq()
print(c)


# In[ ]:




