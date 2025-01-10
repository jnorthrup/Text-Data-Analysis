#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from PIL import Image
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from stylecloud import gen_stylecloud
from gensim import corpora
import pyLDAvis.gensim_models
import gensim
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings(action='ignore')
font_path = 'C:\\Users\\user\\anaconda3\\envs\\text\\Lib\\site-packages\\matplotlib\\mpl-data\\fonts\\malgun.ttf'


# In[14]:


df1=pd.read_csv('data/텍데분전처리2단계끝.csv')
df=df1.copy()
df=df.iloc[:,1:]


# # Topic 

# ### 1. Politics and Law (Election, Government, Law, Prosecution, Murder) about 4000 articles  
# ### 2. Technology (Big Data, AI, Autonomous Driving, Virtual Reality, GPT, Robots) about 2800 articles
# ### 3. Economy (Investment, Companies, Wealth, Stocks, Unemployment, Insurance) about 3000 articles
# ### 4. Environment (Weather, Recycling) about 1000 articles

# #  <font color= red> 1. WordCloud

# ## <font color= green> 1) Politics and Law (Election, Government, Law, Prosecution, Murder) about 4000 articles
# 

# In[33]:


# For slicing, the number of articles per topic was used to find the boundary index with the next topic.
politics= df.iloc[:3848,:].reset_index(drop=True)


# In[35]:


all_data = ''
for _, row in politics.iterrows(): # Object containing row information
    all_data += row['preprocessing_content2']


# In[36]:


all_data


# In[37]:


#https://seaborn.pydata.org/generated/seaborn.color_palette.html
#https://wannabe00.tistory.com/entry/Word-cloud-%EC%9B%90%ED%95%98%EB%8A%94-%EC%83%89%EC%9C%BC%EB%A1%9C-%EA%BE%B8%EB%AF%B8%EA%B8%B0-word-cloud-customize-color
# The above sites were referenced to add to the professor's code and visualize the word cloud.


# In[38]:


mask= np.array(Image.open('투명png/politic.png'))

cloud = WordCloud(font_path = font_path,
                  colormap='gist_rainbow',
                  background_color = 'black',
                  collocations=True,
                  width=2000, height=1000,
                 mask=mask)
my_cloud1 = cloud.generate_from_text(all_data)

arr1 = my_cloud1.to_array()

fig = plt.figure(figsize=(10, 10))
plt.imshow(arr1)
plt.axis('off')
plt.show()
fig.savefig('politics.png') # Save the generated image


# ## <font color = green> 2) Technology (Big Data, AI, Autonomous Driving, Virtual Reality, GPT) about 2800 articles

# In[39]:


tech= df.iloc[3848:6458,:].reset_index(drop=True)


# In[40]:


all_data = ''
for _, row in tech.iterrows(): # Object containing row information
    all_data += row['preprocessing_content2']


# In[41]:


mask= np.array(Image.open('투명png/ai.png'))

cloud = WordCloud(font_path = font_path,
                  colormap='gist_rainbow',
                  background_color = 'black',
                  collocations=True,
                  width=5000, height=4000,
                 mask=mask)
my_cloud1 = cloud.generate_from_text(all_data)

arr1 = my_cloud1.to_array()

fig = plt.figure(figsize=(10, 10))
plt.imshow(arr1)
plt.axis('off')
plt.show()
fig.savefig('tech.png') # Save the generated image


# ## <font color  =green> 3) Economy (Investment, Companies, Wealth, Stocks, Unemployment, Insurance) about 3000 articles

# In[42]:


money=df.iloc[6458:9375,:].reset_index(drop=True)


# In[43]:


all_data = ''
for _, row in money.iterrows(): # Object containing row information
    all_data += row['preprocessing_content2']


# In[44]:


mask= np.array(Image.open('투명png/won.png'))

cloud = WordCloud(font_path = font_path,
                  colormap='gist_rainbow',
                  background_color = 'black',
                  collocations=True,
                  width=5000, height=4000,
                 mask=mask)
my_cloud1 = cloud.generate_from_text(all_data)

arr1 = my_cloud1.to_array()

fig = plt.figure(figsize=(10, 10))
plt.imshow(arr1)
plt.axis('off')
plt.show()
fig.savefig('money.png') # Save the generated image


# ## <font color = green> 4) Environment (Weather, Recycling) about 1000 articles

# In[45]:


env=df.iloc[9375:,:].reset_index(drop=True)


# In[46]:


all_data = ''
for _, row in env.iterrows(): # Object containing row information
    all_data += row['preprocessing_content2']


# In[47]:


mask= np.array(Image.open('투명png/env.png'))

cloud = WordCloud(font_path = font_path,
                  colormap='gist_rainbow',
                  background_color = 'black',
                  collocations=True,
                  width=5000, height=4000,
                 mask=mask)
my_cloud1 = cloud.generate_from_text(all_data)

arr1 = my_cloud1.to_array()

fig = plt.figure(figsize=(10, 10))
plt.imshow(arr1)
plt.axis('off')
plt.show()
fig.savefig('env.png') # Save the generated image


# # <font color= red> 2. Topic Modeling

# In[15]:


# For LDA, it needs to be converted to a list format
df['preprocessing_content2'] = df['preprocessing_content2'].apply(lambda x: x.split())


# In[16]


word_dict = corpora.Dictionary(df['preprocessing_content2'])


# In[17]:


corpus = [word_dict.doc2bow(text) for text in df['preprocessing_content2']]


# In[18]:


len(word_dict)


# ## <font color = red> 2-1) Number of topics: 4 -> Check if topic modeling works well with the initial 4 topics (Politics, Technology, Economy, Environment)

# In[19]:


N_TOPICS = 4
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = N_TOPICS, id2word=word_dict, passes = 15)

topics = ldamodel.print_topics(num_words=4)
for topic in topics:
    print(topic)


# In[20]:


pyLDAvis.enable_notebook()
vis = pyLDAvis.gensim_models.prepare(ldamodel, corpus, word_dict)
pyLDAvis.display(vis)


# ## <font color= red>  2-2) Number of topics: 19 -> Check if more detailed topic modeling is possible with 19 topics

# In[21]:


N_TOPICS = 19
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = N_TOPICS, id2word=word_dict, passes = 15)

topics = ldamodel.print_topics(num_words=4)
for topic in topics:
    print(topic)


# In[22]:


pyLDAvis.enable_notebook()
vis = pyLDAvis.gensim_models.prepare(ldamodel, corpus, word_dict)
pyLDAvis.display(vis)

