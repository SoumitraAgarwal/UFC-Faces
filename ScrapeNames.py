# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd

categories = ['Flyweight', 'Bantamweight','Featherweight', 'Lightweight', 'Welterweight', 'Middleweight', 'Light_Heavyweight', 'Heavyweight']

base1 = 'http://www.ufc.com/fighter/Weight_Class/filterFighters?offset='
base2 = '&weightClass='
base3 = '&fighterFilter=Current'

proxies = {
  'http': 'http://a.soumitra:boo<3ta@202.141.80.22:3128/',
  'https': 'https://a.soumitra:boo<3ta@202.141.80.22:3128/',
}

Name =[]
Url = []
Category =[]

for category in categories:
	
	offset 	= 0
	while(True):
		url 	= base1 + str(offset) + base2 + category + base3
		page 	= requests.get(url,proxies=proxies)
		print(url)
		html 	= page.content
		soup 	= BeautifulSoup(html,'lxml')
		anchs	= soup.findAll('div', class_='fighter-info')

		if(len(anchs) == 0):
			break

		for anch in anchs:
			hr = anch.find('a', class_='fighter-name')
			Name.append(hr.find(text=True).rstrip().lstrip())
			Url.append(hr['href'])
			Category.append(category)

		offset += len(anchs)

temp_df = pd.DataFrame({'Name' : Name,
						'Category' : Category,
						'Url' : Url})
temp_df.to_csv('Mates.csv', index = False, encoding = 'utf-8')

temp_df = pd.read_csv("Mates.csv")
image = []

for i in range(len(temp_df)):
	
	url_temp = 'http://www.ufc.com' + temp_df["Url"][i]
	
	while(True):
		print("Getting page "+ temp_df["Url"][i])
		try:
			page = requests.get(url_temp, proxies=proxies)
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			continue
		break

	html	= page.content
	soup 	= BeautifulSoup(html,'lxml')
	soup 	= soup.find('div',  class_='fighter-image')
	try:
		img		= soup.find('img')
		image.append(img['src'])
	except:
		image.append("0")
		continue

temp_df["Image"] = image
temp_df.to_csv('Names.csv', index = False, encoding = 'utf-8')

