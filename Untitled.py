#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


data=pd.read_csv("weatherHistory.csv")
data


# In[4]:


data.info()


# In[5]:


data.head()


# In[6]:


data.index


# In[8]:


data["Summary"].unique()


# In[9]:


data.head(1)


# In[13]:


data["Temperature (C)"].nunique()


# In[15]:


data["Humidity"].unique()


# In[19]:


data["Summary"] == "Clear"


# In[21]:


data.groupby("Summary").get_group("Clear")


# In[24]:


data[data["Wind Speed (km/h)"] == 3.2039]


# In[29]:


data.isnull().sum()


# In[34]:


data.rename(columns={"Summary":"Weather Comdition"},inplace=True)


# In[35]:


data.head()


# In[36]:


data["Visibility (km)"].mean()


# In[37]:


data["Pressure (millibars)"].std()


# In[39]:


data["Humidity"].var()


# In[41]:


data["Weather Comdition"].value_counts()


# In[48]:


data.nunique()


# In[45]:


data["Weather Comdition"].value_counts()


# In[53]:


data.head()


# In[54]:


data[data["Weather Comdition"]=="Dry"]


# In[56]:


data[data["Weather Comdition"].str.contains("Dry")]


# In[ ]:




