#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import numpy library
import numpy as np 
# Create 1D numpy array
x = np.array([45,67,57,60])
print(x)
print(type(x))
print(x.dtype)


# In[3]:


# Verify the data type 
x = np.array(["A",67,57,9.8])
print(x)
print(type(x))
print(x.dtype)


# In[6]:


# Create a 2D array
a2 = np.array([[20,40],[30,40]])
print(a2)
print(type(a2))
print(a2.shape)


# In[7]:


#Reshaping an array
a = np.array([10,20,30,40])
b = a.reshape(2,2)
print(b)
print(b.shape)


# In[8]:


#Use of np.sqrt()
d = np.array([1.654,3.76543,4.4324])
print(d)
print(np.around(np.sqrt(d),2))


# In[9]:


a1 = np.array([[3,4,5,8],[7,2,8, np.NAN]])
print(a1)
print(a1.shape)
a1.dtype


# In[10]:


#Mathematical opereations on rows and cols
a2 = np.array([[3,4,6],[7,9,10],[4,6,12]])
a2


# In[12]:


print(a2)
print(a2.mean(axis = 0))
print(a2.mean(axis = 1))


# In[5]:


import numpy as np
# Matrix operations
a3 = np.array([[3,4,5],[7,2,8],[9,1,6]])
print(a3)
np.fill_diagonal(a3,0)
print(a3)


# In[7]:


#Define two matrices and multiply them
A = np.array([[1,3],[2,4]])
B = np.array([[5,6],[7,8]])
print(A.T)
print(B.T)


# In[8]:


a4 = np.array([[3,4,5],[7,2,8],[9,1,6],[10,9,18]])
a4


# In[ ]:




