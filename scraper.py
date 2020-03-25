from splinter import Browser
from bs4 import BeautifulSoup
import os
import re

table_columns: ['country_other', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_recovered', 'active_cases']

def init_browser():
	executable_path={'executable_path': 'C:/Users/kevin/Documents/Python/chromedriver'}
	return Browser('chrome', **executable_path, headless=False)

def scrape_to_html():
	# browser=init_browser()
	# listings={}
	# url='https://www.worldometers.info/coronavirus/'
	# browser.visit(url)
	# soup=BeautifulSoup(browser.html, 'html.parser')
	# table=soup.find('table', id_='main_table_countries_today')
	# print(table['class'])
	filepath = os.path.join("worldometer.html")
	with open(filepath, encoding='utf-8') as file:
		html = file.read()
	soup=BeautifulSoup(html, 'html.parser')
	table=soup.find('table', id='main_table_countries_today')
	table_column_heads=[]
	for each_head in table.find('thead').find_all('th'):
		table_column_heads.append(each_head.text.strip())
	# table_columns=['country_other', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_recovered', 'active_cases', 'serioues_critical', 'tot_cases_per_1M_pop']
	table_data_list=[]
	# i=0
	for each_row in table.find('tbody').find_all('tr'):
		i=0
		# row_data={}
		row_data_list=[]
		for each_cell in each_row.find_all('td'):
			data_value=each_cell.text.strip()
			if not i == 0:
				data_value=re.sub('[^\d\.]', '', data_value)
				try: 
					data_value=int(data_value)
				except: 
					pass
			# row_data[table_columns[i]]=data_value
			row_data_list.append(data_value)
			i+=1
		# table_data.append(row_data)
		table_data_list.append(row_data_list)
	html_string='<table>'
	html_string=html_string+'<thead>'+'<tr><td>'+'</td><td>'.join(table_column_heads)+'</td></tr>'+'</thead>'
	html_string=html_string+'<tbody>'
	for row in table_data_list:
		row_in_str=[str(data) for data in row]
		html_string=html_string+'<tr><td>'+'</td><td>'.join(row_in_str)+'</td></tr>'
	html_string=html_string+'</tbody>'
	return html_string