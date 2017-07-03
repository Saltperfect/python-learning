import requests
from bs4 import BeautifulSoup

def word_finder(url):
	word_list = []
	source_code = requests.get(url).text
	soup = BeautifulSoup(source_code, 'html_parser')
	text = soup.get_text()
	print (soup.get_text())

word_finder('http://www.azlyrics.com/lyrics/twentyonepilots/implicitdemandforproof.html')