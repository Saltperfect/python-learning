from urllib import request
fab_url = 'https://www.ibm.com/support/knowledgecenter/en/SVU13_7.2.1/com.ibm.ismsaas.doc/reference/AssetsImportCompleteSample.csv?view=kc'
def csv_download(url):
	response = request.urlopen(url)
	csv = response.read()
	csv_str = str(csv)
	lines = csv_str.split('\\n')
	dest_url = r'fab.csv'
	fw = open (dest_url , 'w')
	for line in lines:
		fw.write(line + '\n')
	fw.close
	print (response)
	#print (csv_str)
	print (lines)

csv_download(fab_url)


