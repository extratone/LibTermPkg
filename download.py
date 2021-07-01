import requests
import sys
import os

def download_file(path):
	r = requests.get(path)
	filename = path.split("/")[-1]
	fullname = str(os.getcwd())+"/"+filename
	 
	with open(fullname, 'wb') as f:
		f.write(r.content)
		print ("File downloaded: " + str(filename))
 
try:
	if sys.argv[1]:
		download_file (sys.argv[1])
	else:
		print("no url file found")
except IndexError:
	print("Usage: download <url_file>")