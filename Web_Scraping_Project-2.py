#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import os


# In[2]:



url = 'https://quotes.toscrape.com/tag/life/'


# In[3]:


#get url
res = requests.get(url)


# In[4]:


res


# In[5]:


# parse HTML content
content = BeautifulSoup(res.content, 'html.parser')


# In[6]:


content


# In[7]:


#extract all div and class elements
quotes = content.find_all('div', class_='quote')


# In[8]:


#empty list
quote_file = []

# write for loop to extact data and append it to empty list
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    link = quote.find('a')
    quote_file.append([text, author, link['href']])


# In[9]:


quote_file


# In[10]:


#convert list to dataframe
df = pd.DataFrame(quote_file)


# In[11]:


df


# In[12]:


# remove index,give columns header and export as csv
df.to_csv('/Users/derya_ak/Desktop/quotes.csv', index=False, header=['quote','author', 'link'])


# In[13]:


import os

file_name = "Web_Scraping_Project.ipynb"

os.system(f"jupyter nbconvert --to script {file_name}")


# In[ ]:





# In[ ]:





# In[ ]:




