import requests

import pandas as pd

from bs4 import BeautifulSoup as bs

import csv

url = "https://economictimes.indiatimes.com/tata-consultancy-services-ltd/stocksupdate/companyid-8345.cms"

response = requests.get(url)

html = response.text

# print(html)

soup = bs(html,"lxml")

tables = soup.findAll('div',attrs={'class':'eachStory'})

#print(tables)

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



# table  = soup.find('div',attrs={'class':'all'})

#print(table.contents[0].attrs.class)

# for tag in table.findChildren():
# 	#print(tag.attrs.get('class'))
# 	if tag.attrs.get('class') is ['mktDiv']:
# 		tag.clear()


# table1 = table.children

# if(table.findAll(id='BSEDiv')!=[] || table.findAll)

# listR=[]
# for row in table.findAll('tr'):
# 	listC = []
# 	for head in row.findAll('th'):
# 		listC.append(head.text)
# 	for col in row.findAll('td'):
# 		listC.append(col.text)
# 		# print(col.text)
# 	listR.append(listC)
# print(listR)

# outfile  = open("premiertable.csv","w")

# writer  = csv.writer(outfile)

# # writer.writerows(['Pos',"Club","P","W",'D',"L","GD","Pts"])

# writer.writerows(listR)

# print(table.text)