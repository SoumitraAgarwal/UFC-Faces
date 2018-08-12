# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd
import shutil
import os

df = pd.read_csv("Names.csv")

print("Read complete")

url = 'http://'

proxies = {
  'http': 'http://a.soumitra:boo<3ta@202.141.80.22:3128/',
  'https': 'https://a.soumitra:boo<3ta@202.141.80.22:3128/',
}


for i in range(len(df)):
	url_temp = url+df['Image'][i][2:]
	print(url_temp)
	while(True):
		try:
			response = requests.get(url_temp, stream=True,proxies=proxies)
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			continue
		break

	print(df['Name'][i])
	if(df['Category'][i] not in os.listdir('.')):
		os.mkdir(df['Category'][i])
	
	with open(df['Category'][i] + '/' + df['Name'][i]+'.png', 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response