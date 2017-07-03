import requests
from bs4 import BeautifulSoup

def crawler():
	#page = 1
	#while page <= max_pages:
		url = 'http://o2tvseries.com/13-Reasons-Why/Season-01/index.html'
		source_code = requests.get(url)
		plain_text = source_code.text
		#print(plain_text)
		soup = BeautifulSoup(plain_text , 'html.parser')
		for link in soup.findAll('div', {'class': 'data'}):
			href = link.get('href')
			title = link.string
			print(href)
			print(title)
		#page +=1

crawler()
print ('sunday!')