#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


x = [1, 1.2, 2.3, 4, 5]
y = [9, -8, 3, 4, 5]


# In[3]:


plt.plot(x,y)


# In[8]:


np.random.randint(1, 10, 10)


# In[11]:


x = np.random.randn(100)
x.mean()
x.std()


# In[12]:


plt.plot(x)


# In[14]:


x = x + 37


# In[15]:


x = x - 37


# In[16]:


x = 5*x + 37
x.mean()


# In[17]:


x.std()


# In[18]:


x = np.linspace(0,10,200)


# In[19]:


y = np.sin(x) + 0.8*x


# In[20]:


plt.plot(x,y)


# In[33]:


y = np.sin(x) + 0.8*x +0.4*np.random.randn(200)


# In[34]:


plt.scatter(x,y)


# In[32]:


## Markdown ##


# In[35]:


# 加註解練習


# # 最大標題
# ## 第二大標題
# ### 第三大
# 
# 隨便搞操你媽
# 
# 連續技: cntl+m, m

# ### 分點說明
# 
# * Python
# * Matplotlib
# * Numpy
# * pandas

# ### 有順序的分項
# 
# 1. PYthon
# 1. Matplotlib
# 1. Numpy

# ### 做超連結
# 
# [課程線上超連結]
# (http://bit.ly/iWantPython)

# # 圖片要放在同一個資料夾之下
# ![圖片](248634.jpg)

# In[ ]:




