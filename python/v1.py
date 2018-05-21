import requests as re
from bs4 import BeautifulSoup as bs
headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

url = 'https://www.bbcgoodfood.com/'

re.get(url,headers = headers)

soup = bs(re.text,'html.parser')

print ('\n'.join(map(lambda x:x['href'],soup.find_all('a'))))


