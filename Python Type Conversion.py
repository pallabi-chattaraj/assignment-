#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q1: Convert an integer to a floatig-point number>>>


# In[2]:


num = 7
print(type(num))

float_num = float(num)
print(type(float_num))
print(float_num)


# In[ ]:


# Q2:Covert a float to a iteger>>>


# In[5]:


import math
num = 7.6
print(type(num))
print(num)

floor_value = math.floor(num)
ceil_value = math.ceil(num)
print(type(floor_value))
print(floor_value)
print(type(ceil_value))
print(ceil_value)


# In[ ]:


#Q3: Convert an integer to a string>>>


# In[9]:


Num = 10
print(type(Num))
float_num = float(Num)
print(type(float_num))
print(float_num)



# In[ ]:


#Q4: Convert a list to a tuple>>>


# In[12]:


my_list= [30 , 40 , 10, 20 , 4.6, "ram", "madhu" , "akash"]
print(type(my_list))

my_tuple= tuple(my_list)
print(type(my_tuple))
print(my_tuple)


# In[ ]:


#Q5: Convert a tuple to a list>>>


# In[18]:


my_tuple= (20 , 30 , - 40, "shreyashi","puja","binay",[2, 3, 5] , 5.7 )

print(type(my_tuple))

print(my_tuple)

my_list= list(my_tuple)

print(type(my_list))

print(my_list)


# In[ ]:


#Q6: Convert a decimal number to binary>>>


# In[19]:


num = 156
bin(num)


# In[ ]:


#Q7:Convert a non-zero number to boolean>>>


# In[21]:


num = 10
boolean_num= bool(num)

print(type(boolean_num))
print(boolean_num)


# In[ ]:




