<h2 align='center'> Extracting Key Features through Word Cloud and Topic Analysis using LDA for Major Current Affairs </h2>
<h3 align='center'> [Major] Text Data Analysis Project </h3>
<h4 align='center'> (May 2023 ~ June 2023) </h4> 

![Aqua Lines](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

&nbsp;

## 1. Background and Purpose

- Extracting key features and topic analysis through crawling Naver News articles
- Extracting key features through Word Cloud and topic analysis using LDA for major current affairs focusing on politics and law, technology, economy, and environment

<br/>

## 2. Organizing Institution

- Organizer: AI Big Data Convergence Management Department Major Course 'Text Data Analysis'

<br/>

## 3. Project Duration 
- May 2023 ~ June 2023 (2 months)


<br/>

## 4. Project Description 
<img width="530" alt="텍데분1" src="https://github.com/Ji-eun-Kim/Text-Data-Analytics/assets/124686375/8ecd0c22-ff86-476c-84d1-6b114c25c668"> | <img width="530" alt="텍데분2" src="https://github.com/Ji-eun-Kim/Text-Data-Analytics/assets/124686375/1e79b8af-1965-480c-843e-226631ba4f54"> 
---|---|

<img width="533" alt="텍데분3" src="https://github.com/Ji-eun-Kim/Text-Data-Analytics/assets/124686375/fa577161-e59f-4d56-b2f0-226cfe4b503b"> | <img width="533" alt="텍데분4" src="https://github.com/Ji-eun-Kim/Text-Data-Analytics/assets/124686375/a1c33180-9ff0-4ab5-8bb5-f23ddc32e228"> 
---|---|

This project was conducted by collecting text data on more than 5 topics of interest and securing at least 10,000 data. The project was conducted under the theme of 'Extracting Key Features through Word Cloud and Topic Analysis using LDA for Major Current Affairs'. For data collection, Naver News articles were crawled using Naver OpenAPI. The articles were chosen because they are verified for spelling and are widely read by the public. The main topics were politics and law, technology, economy, and environment. Using BeautifulSoup (bs4) and Selenium, a total of 10,400 data were collected after removing duplicates.

For preprocessing, basic stopwords.txt was used to remove spaces, English, and special characters. Morphological analysis was also performed using Konlpy. Additionally, a second round of stopword processing was conducted. Using value_counts(), unnecessary particles (e.g., '도', '이다', '은', '돼다', '하고') were removed. Furthermore, unnecessary words frequently mentioned in articles (e.g., '기자', '제보', '저자', '방송', '화면', '캡처', '리포트', '영상편집', '채널', '구독', '뉴스데스크', '화면', '현지', '시각', '연합뉴스') and reporter names (e.g., '앙카라', '로이터') were also removed.

For visualization, Word Cloud was used to analyze the key features of each topic. The results showed that in the political field, keywords such as 'veto', 'nursing', and 'President Yoon' were frequently mentioned, indicating current issues in the government and parliament. In the technology field, terms like 'generation', 'development', and 'provision' were frequently mentioned, indicating terms used in the software industry. Additionally, time-related terms such as 'currently', 'this year', 'recently', and 'new' were frequently mentioned, indicating sensitivity to the passage of time. In the economic field, terms like 'investment securities', 'USA', and 'company' were frequently mentioned, indicating economic terms. Time-related terms such as 'recently', 'last', 'this year', and 'currently' were also frequently mentioned, indicating sensitivity to the passage of time. In the environmental field, keywords such as 'weather' and 'recycling' were frequently mentioned. For weather-related topics, terms like 'daytime', 'temperature', 'lowest', and 'highest temperature' were frequently mentioned. For recycling-related topics, terms like 'waste plastic', 'waste battery', and 'resource circulation' were frequently mentioned.

For topic analysis, LDA was used instead of LSA due to its advantages in visualization and overcoming the limitations of LSA. The main topics were 4, so n_topics=4 was set to see if the topic analysis was well done for the 4 fields. The results showed that the topic analysis was well done for each topic. Additionally, it was confirmed that setting a higher n_topics allows for more detailed topic analysis.

After conducting the project, there were two main limitations and insights: 1. Lack of time compared to the amount of work, 2. Diversity of crawling. If there was more time, stopword processing could have been done more neatly. The model took about 6 days to run, leaving a lot of regret. For the diversity of crawling, only Naver News articles were used, but there was a desire to analyze YouTube comments or netizen comments as well.

<br/>

## 5. Team Members and Roles  

<Team Members>  
- Individual Project  

<br>
  
<Roles>    
- Crawling about 10,400 Naver News articles using Naver Open API (politics, technology, economy, environment)
- Morphological analysis and stopword processing using Konlpy
- Analyzing key features of each topic using Word Cloud
- Topic analysis using LDA (checking results by adjusting n_topics parameter)

<br/>

## 6. Presentation Materials and Data

- Presentation Materials  
https://drive.google.com/file/d/11RzQESiiQE40Ko6wUCFMtDZ2B0AX_ngI/view

- Data  
https://drive.google.com/drive/folders/1JhLosohVZVdgDfT44aNN3qAU3Vb48YIx?usp=drive_link

