
from bs4 import BeautifulSoup as bs
import re as reg
import requests as re
def fetchFromServer(URL):
    headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    #The next line should be considered sacrid only run when absolutly needed
    r = re.get(URL,headers = headers)
    #would be better to have a db connection
    assert(r.text!=None)
    #store(URL,r.text)
    return r.text

f = open('../bbcgoodfood.xml','r')
soup= bs(f.read(),'xml')
f.close()
locs = soup.find_all('loc')
errors = []
skip = True
for loc in locs:
    url = loc.get_text()
    print(url)
    if url == 'https://www.bbcgoodfood.com/recipe/veggie-lasagne-0':
        skip = False
    if url[:34]=='https://www.bbcgoodfood.com/recipe' and not skip:
        id_group  = reg.match('.*\/(\d+)\/.*',url)
        try:
            id_ = id_group.group(1)
            page = fetchFromServer(loc.get_text())
            f = open('bbcgoodfood/%s'%id_,'w')
            f.write(page)
            f.close()
        except:
            errors.append(url)

print ("Errors")
print (errors)
