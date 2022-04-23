import requests
from bs4 import BeautifulSoup
import pandas as pd

topic_url ="https://github.com/topics"
response =requests.get(topic_url)
response.status_code
page_contents= response.text
#with open('webpage.html','w') as f:
   # f.write(page_contents) 
doc= BeautifulSoup(page_contents,'html.parser')
topic_title_tags = doc.find_all('p',
    {'class':'f3 lh-condensed mb-0 mt-1 Link--primary'})
topic_titile_desc =doc.find_all('p',{'class':'f5 color-fg-muted mb-0 mt-1'})
topic_title_links =doc.find_all('a',{'class':'no-underline flex-grow-0'})

topic_titles=[]
topic_desc=[]
topic_urls=[]
for tag in topic_title_tags:
    topic_titles.append(tag.text)
for tag in topic_titile_desc:
    topic_desc.append(tag.text.strip())
for tag in topic_title_links:
    topic_urls.append('https://github.com'+tag['href'])

topic_dict={'title':topic_titles,'desccription':topic_desc,'url':topic_urls}
topic_df=pd.DataFrame(topic_dict)

topic_df.to_csv('topics.csv')