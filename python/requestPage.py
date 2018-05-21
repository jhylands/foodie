import requests as re
import JSON
headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

url = 'https://www.bbcgoodfood.com/'

#check the data file to see if there already exists a file under this request
with  open('../cacheCheck.dat','r') as f:
    cache = JSON.decode(f.read())
if(url in cache):
    bit = False 

#The next line should be considered sacrid only run when absolutly needed
if bit:
    re.get(url,headers = headers)
    #would be better to have a db connection
    cache[url] = filething
else:
    print "File not requested some error occured. This may be as a resut of :"
    print "-The file has already been requesed and is cached"
    print "-A similar file has already been cached"

