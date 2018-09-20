import requests

import pandas as pd

from bs4 import BeautifulSoup as bs

import csv

url = "https://economictimes.indiatimes.com/tata-consultancy-services-ltd/stocksupdate/companyid-8345.cms"

response = requests.get(url)

html = response.text


soup = bs(html,"lxml")

tables = soup.findAll('div',attrs={'class':'eachStory'})


records=[]

for table in tables:
	date=table.find('time').text[:11]
	title=table.find('p').text
	url='https://economictimes.indiatimes.com/' + table.find('a')['href']
	#print(url)	
	records.append((date,title,url))

df = pd.DataFrame(records)

df.columns=['Date','News','Url']

df['Date'] = pd.to_datetime(df['Date'])

df.to_csv('tcs_news.tsv', encoding='utf-8',sep='\t')

print(df)



