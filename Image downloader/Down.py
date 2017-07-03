import random
import urllib.request

def downloader(url):
	name = random.randrange(1,1000)
	full_name = str(name) + '.jpg'
	urllib.request.urlretrieve(url, full_name)

downloader('http://www.twentyonepilots.com//sites/g/files/g2000004896/f/201505/official-og-image.jpg')

