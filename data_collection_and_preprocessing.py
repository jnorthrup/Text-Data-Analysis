#!/usr/bin/env python
# coding: utf-8

# In[226]:


from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
import os
import sys
import urllib.request
import json
import re
import time
import pandas as pd
import nltk
from tqdm import tqdm
from konlpy.tag import Okt
from nltk.tokenize import word_tokenize

#driver = webdriver.Chrome('D:\MyWorkspace\chromedriver.exe')


# # 1. Data Collection

# ## <font color= 'red'> 0) BASE CODE <Function Definition, Naver News Article Crawling>

# In[8]:


def remove_tag(my_str):
    ## Function to remove tags
    p = re.compile('(<([^>]+)>)')
    return p.sub('', my_str)

def sub_html_special_char(my_str):
    ## Convert special characters represented by &apos;, &quot to actual special characters
    p1 = re.compile('&lt;') # Convert lt to <
    p2 = re.compile('&gt;')
    p3 = re.compile('&amp;')
    p4 = re.compile('&apos;')
    p5 = re.compile('&quot;')

    result = p1.sub('\<', my_str)
    result = p2.sub('\>', result)
    result = p3.sub('\&', result)
    result = p4.sub('\'', result)
    result = p5.sub('\"', result)
    return result


# In[9]:


base_url = 'https://openapi.naver.com/v1/search/news.json'

def getresult(client_id,client_secret,query,n_display,start,sort='sim'):
    encQuery = urllib.parse.quote(query)
    
    url = f'{base_url}?query={encQuery}&display={n_display}&start={start}&sort={sort}'
    my_request = urllib.request.Request(url)
    my_request.add_header("X-Naver-Client-Id",client_id)
    my_request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(my_request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        search_result_str = response_body.decode('utf-8')
        search_results = json.loads(search_result_str)
    else:
        print("Error Code:" + rescode)
    return search_results['items']


# In[10]:


# Some parts of the data collection process were collaborated with fellow student Bae Min-sung.
# The code shared by fellow student Lee Soo-in on Slack was also referenced.
def search_news_with_link (result):
    article_ids = ['dic_area']
    titles = []
    links = []
    pubdates = []
    contents = []

    p = re.compile('https://n.news.naver.com/.+')
    for i, item in enumerate(result):
        if p.match(item['link']): ## Extract only results where the <link> tag string starts with n.news.naver.com/
            title = sub_html_special_char(remove_tag(item['title']))
            link = item['link']
            pubdate = item['pubDate']
            titles.append(title)
            links.append(link)
            pubdates.append(pubdate)

            html = urllib.request.urlopen(link)
            bs_obj = BeautifulSoup(html, 'html.parser')
            for article_id in article_ids:
                print(article_id)
                content = bs_obj.find_all('div', {'id':article_id})
                if len(content) > 0:
                    contents.append(content[0].text)
                    break
                else:
                    contents.append(0)
                    # To avoid collecting entertainment news and similar articles, the above code was written.
                    # If the main text id is not dic_area, it is filled with 0 and deleted after collecting all data.
                    # If the value is not filled with 0 when adding to the dataframe, the dataframe will not be created (length issue).
                
    result_dict = {'title': titles, 'link': links, 'pubdate': pubdates, 'content': contents}
    df = pd.DataFrame.from_dict(result_dict)
    return df


# In[11]:


client_id = '03xivz4Z_LC7mSS5tkO6'
client_secret = 'uvknoLe1Jq'
n_display=100


# # <font color= 'red'> 1) Data Crawling - 4 Topics 

# ### 1. Politics and Law (Election, Government, Law, Prosecution, Murder)  
# ### 2. Technology (Big Data, AI, Autonomous Driving, Virtual Reality, GPT, Robot)  
# ### 3. Economy (Investment, Company, Wealthy, Stock, Unemployment, Insurance)  
# ### 4. Environment (Weather, Recycling)  

# # 1. Politics and Law (Election, Government, Law, Prosecution, Murder)

# # Presidential Election

# In[22]:


query = '대선'


# In[23]:


# Some parts of the code were collaborated with fellow student Bae Min-sung.
# The code shared by fellow student Lee Soo-in on Slack was also referenced.
total_results = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results = pd.concat([total_results, up_result])
    print(len(total_results))


# In[24]:


total_results.reset_index(drop=True, inplace=True)


# # Government

# In[15]:


query = '정부'


# In[16]:


total_results2 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results2 = pd.concat([total_results2
                                , up_result])
    print(len(total_results2))


# In[18]:


total_results2.reset_index(drop=True, inplace=True)


# # Law

# In[25]:


query = '법'


# In[26]:


total_results3 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results3 = pd.concat([total_results3, up_result])
    print(len(total_results3))


# In[27]:


total_results3.reset_index(drop=True, inplace=True)


# # Prosecution

# In[30]:


query = '검찰'


# In[32]:


total_results4 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results4 = pd.concat([total_results4, up_result])
    print(len(total_results4))


# In[33]:


total_results4.reset_index(drop=True, inplace=True)


# # Murder

# In[35]:


query = '살인'


# In[36]:


total_results5 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results5 = pd.concat([total_results5, up_result])
    print(len(total_results5))


# In[37]:


total_results5.reset_index(drop=True, inplace=True)


# # 2. Technology (Big Data, AI, Autonomous Driving, Virtual Reality, gpt, Robot)

# # Big Data

# In[39]:


query = '빅데이터'


# In[40]:


total_results6 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results6 = pd.concat([total_results6, up_result])
    print(len(total_results6))


# In[41]:


total_results6.reset_index(drop=True, inplace=True)


# # AI

# In[43]:


query = 'AI'


# In[44]:


total_results7 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results7 = pd.concat([total_results7, up_result])
    print(len(total_results7))


# In[45]:


total_results7.reset_index(drop=True, inplace=True)


# # Autonomous Driving

# In[46]:


query = '자율주행'


# In[48]:


total_results8 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results8 = pd.concat([total_results8, up_result])
    print(len(total_results8))


# In[49]:


total_results8.reset_index(drop=True, inplace=True)


# # Virtual Reality

# In[50]:


query = '가상현실'


# In[52]:


total_results9 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results9 = pd.concat([total_results9, up_result])
    print(len(total_results9))


# In[53]:


total_results9.reset_index(drop=True, inplace=True)


# # gpt

# In[54]:


query = 'gpt'


# In[55]:


total_results10 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results10 = pd.concat([total_results10, up_result])
    print(len(total_results10))


# # Robot

# In[90]:


query = '로봇'


# In[91]:


total_results11 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results11 = pd.concat([total_results11, up_result])
    print(len(total_results11))


# In[92]:


total_results11.reset_index(drop=True, inplace=True)


# # 3. Economy (Investment, Company, Wealthy, Stock, Unemployment, Insurance)

# # Investment

# In[93]:


query = '투자'


# In[95]:


total_results12 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results12 = pd.concat([total_results12, up_result])
    print(len(total_results12))
    


# In[96]:


total_results12.reset_index(drop=True, inplace=True)


# # Company

# In[97]:


query = '기업'


# In[98]:


total_results13 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results13 = pd.concat([total_results13, up_result])
    print(len(total_results13))


# In[99]:


total_results13.reset_index(drop=True, inplace=True)


# # Wealthy

# In[100]:


query = '부자'


# In[101]:


total_results14 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results14 = pd.concat([total_results14, up_result])
    print(len(total_results14))


# In[102]:


total_results14.reset_index(drop=True, inplace=True)


# # Stock

# In[103]:


query = '주식'


# In[104]:


total_results15 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results15 = pd.concat([total_results15, up_result])
    print(len(total_results15))


# In[105]:


total_results15.reset_index(drop=True, inplace=True)


# # Unemployment

# In[116]:


query = '실업'


# In[117]:


total_results16 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results16 = pd.concat([total_results16, up_result])
    print(len(total_results16))


# In[118]:


total_results16.reset_index(drop=True, inplace=True)


# In[109]:


middle= pd.concat([total_results, total_results2,total_results3,total_results4,
                  total_results5,total_results6,total_results7,total_results8,
                  total_results9,total_results10,total_results11,total_results12,
                  total_results13,total_results14,total_results15,total_results16])


# In[111]:


# Check the number of data collected
middle.shape


# # Insurance

# In[119]:


query = '보험'


# In[120]:


total_results17 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results17 = pd.concat([total_results17, up_result])
    print(len(total_results17))


# In[121]:


total_results17.reset_index(drop=True, inplace=True)


# In[122]:


middle= pd.concat([total_results, total_results2,total_results3,total_results4,
                  total_results5,total_results6,total_results7,total_results8,
                  total_results9,total_results10,total_results11,total_results12,
                  total_results13,total_results14,total_results15,total_results16,
                  total_results17])


# In[124]:


middle.shape


# # 4. Environment (Weather, Recycling)

# # Weather

# In[129]:


query = '날씨'


# In[130]:


total_results18 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results18 = pd.concat([total_results18, up_result])
    print(len(total_results18))


# In[131]:


total_results18.reset_index(drop=True, inplace=True)


# # Recycling

# In[132]:


query = '재활용'


# In[134]:


total_results19 = pd.DataFrame()
for i in range(10):
    start=1+n_display*i
    print(start)
    result= getresult(client_id,client_secret,query,n_display,start,sort='sim')
    up_result = search_news_with_link(result)
    
    total_results19 = pd.concat([total_results19, up_result])
    print(len(total_results19))


# In[135]:


total_results19.reset_index(drop=True, inplace=True)


# # Concat

# In[136]:


crawl= pd.concat([total_results, total_results2,total_results3,total_results4,
               total_results5,total_results6,total_results7,total_results8,
              total_results9,total_results10,total_results11,total_results12,
               total_results13,total_results14,total_results15,total_results16,total_results17,
                 total_results18, total_results19])


# In[137]:


crawl.shape


# In[138]:


crawl.reset_index(drop=True, inplace=True)


# ## <font color = 'red'> 2) Text Data Preprocessing

# ## <font color= red> 2-1) Cleaning

# #### Rows with content equal to 0 are Naver entertainment news, and to remove articles corresponding to entertainment news, they are added as 0 and deleted.
# - To crawl only Naver news articles, articles with main text ids not corresponding to dic_area were added as 0 in the content.
# - Additionally, I wanted to use continue to skip ids that do not correspond, but it did not work well, and as a result, when converting to a dictionary, the title appeared, but since it is an article without an id, the content was empty, causing an issue where the dataframe could not be created.
# - Therefore, preprocessing was conducted in a way to fill with 0 and delete as described above.

# ### Remove rows with content equal to 0

# In[139]:


cl= crawl.copy()


# In[140]:


cl.head()


# In[141]:


cl.drop(cl.loc[cl['content']==0].index, inplace=True)


# ## <font color=red> 2-2) Remove Duplicates

# In[142]:


cl=cl.drop_duplicates()


# In[143]:


cl.reset_index(drop=True,inplace=True)


# In[144]:


cl[cl.duplicated(keep=False)]


# In[145]:


cl.shape


# ## Save 1st DataFrame

# In[149]:


cl.to_csv('crawling_df.csv',index=False)


# ## Load Data

# In[2]:


df=pd.read_csv('crawling_df.csv')


# In[3]:


df1=df.copy()


# ## <font color = red> 3) 1st Data Preprocessing - Stopwords, Stemming

# In[5]:


import copy
from konlpy.tag import Okt
import pykospacing
import kss
with open ('stopwords.txt','r',encoding='utf-8')as f:
    stopwords= f.readlines()
stopwords= [x.replace('\n','') for x in stopwords]
okt=Okt()


# In[6]:


df1.info()


# In[7]:


# Using the existing stopwords.txt from the professor, perform the first stopword removal and stemming
def preprocess_korean(text):
    my_text=copy.copy(text)
    # Remove \n
    my_text = my_text.replace('\n','')
    spacer= pykospacing.Spacing() # Correct spacing
    my_text=spacer(my_text)
    sents=kss.split_sentences(my_text)
    
    p=re.compile('[^ㄱ-ㅎㅏ-ㅣ가-힣]') # All characters except Korean and spaces
    results=[]
    for sent in tqdm(sents):
        result=[]
        tokens= okt.morphs(sent, stem=True) # Stemming
        for token in tokens:
            token=p.sub('',token)
            if token not in stopwords: # Add only those not in stopwords
                result.append(token) 
        results.extend(result) 
    result= ' '.join(results)
    
    return result  


# In[8]:


# It took about 6 days
df1['preprocessing_content']= df1['content'].apply(lambda x: preprocess_korean(x))


# In[196]:


df1.to_csv('텍데분전처리1단계끝.csv',index=False)


# ## <font color= red> 4) 2nd Stopword Removal - Collect additional stopwords based on the results from the 1st preprocessing

# In[227]:


df1=pd.read_csv('텍데분전처리1단계끝.csv')


# In[228]:


df=df1.copy()


# ###  <font color = red> 4-1) Delete rows with empty content after the 1st preprocessing

# In[231]:


df.isnull().sum()


# In[232]:


# After the 1st preprocessing, rows with empty content can be seen
df.iloc[[161]]


# In[233]:


df=df.dropna(axis=0)


# In[234]:


df.reset_index(inplace=True,drop=True)


# In[236]:


df.isnull().sum()


# In[237]:


len(df)


# ### <font color = red> 4-2) Save tokens from the 1st preprocessing into a list and perform the 2nd stopword removal

# In[238]:


stopwords2= []
for i in tqdm(range(len(df))): #0~10377
    for value in list(df.preprocessing_content[i].split(' ')): 
        stopwords2.append(value) # Save tokens assigned to 10400 articles into stopwords2


# In[239]:


imsi=pd.DataFrame(stopwords2)
imsi=imsi.rename(columns={0:'words'})


# In[240]:


# Extract the most frequently occurring stopwords and save them into a new stopword list (mainly top 30 particles)
word= pd.DataFrame(imsi['words'].value_counts()).head(30).index.tolist()


# In[241]:


# Extract stopwords with a value_counts of one and save them into a new stopword list (bottom 30)
word2=pd.DataFrame(imsi['words'].value_counts()).tail(30).index.tolist()


# In[242]:


stopwords2_total=word+word2


# In[243]:


# Remove meaningful words from the stopwords list
rm_set = {'대통령', '기업','기술','법','투자','서울'}
# Use list comprehension to compare with the set of words to be deleted
stopwords2_total = [i for i in stopwords2_total if i not in rm_set]
print(stopwords2_total)


# In[244]:


# Additionally, while looking for common unnecessary stopwords in the tokens assigned to articles (about 150 articles were used as examples), add them to the list
stopwords3= ['',' ', '기자','무단','앙카라','로이터','뉴스','금지','무단','뉴스','제보','저자','방송','화면','캡처','사진','방송화면',
            '연합뉴스','왼쪽부터','데일리안','현지','시각','시간','기사내용','뉴시스','뉴스데스크','카카오톡','기','다리다','이메일',
            '앵커','자료조사','영상편집','리포트','채널','네이버','유튜브','구독','카카오','톡','전화','추가','영상','디자인',
            '페이스북','트위터','노컷뉴스','사이트','기사','내용','요약','출처','은','는','이','가','이다','하다','돼다','에','에서',
             '에선','라며','고','하','다','하고','하며','되다','뉴욕타임즈','오다','보다','따르다','가다','통해','에는','없다','대한',
             '때문','관련','경우','이르다','그렇다','에서는','뿐 아니다','지다','들다','대다','보이다','에도','이나','아니다',
             '씨','김','데','시','날','면서']


# In[245]:


# Compare with the additional stopwords found and add any missing stopwords
for i in stopwords3:
    if i not in stopwords2_total:
        stopwords2_total.append(i)


# In[246]:


stopwords2_total=' '.join(stopwords2_total)


# In[247]:


#https://junjun-94.tistory.com/18
# Using this link, I understood the code and converted it into a function to write the additional stopword processing code.
def preprocess_korean2(example):
    stop_words = stopwords2_total
    stop_words = stop_words.split(' ')

    word_tokens =word_tokenize(example)
    
    result=[]
    for w in tqdm(word_tokens):
        if w not in stop_words:
            result.append(w)
    
    result = ' '.join(result)
 

    return result


# In[248]:


df['preprocessing_content2']= df['preprocessing_content'].apply(lambda x: preprocess_korean2(x))


# In[249]:


df1=df.copy()


# In[250]:


# Delete articles with empty content
df1.query('preprocessing_content2==""')


# In[251]:


df1.drop([2844,4654,5608,5876,7782], axis=0,inplace=True)


# In[252]:


df1=df1.reset_index(drop=True)


# In[253]:


df1.to_csv('텍데분전처리2단계끝.csv')


# In[1]:


import pandas as pd


# In[4]:


pd.read_csv('data/텍데분전처리2단계끝.csv')['preprocessing_content2']


# In[27]:


pd.read_csv('data/텍데분전처리2단계끝.csv').iloc[:,1:].shape

