import re as reg 
import requests as re
from tesco_spider import GrocerySpider
from bs4 import BeautifulSoup as bs


class _getText():
	def get_text(self):
		return ''
def try1(e):
	try:
		return e[1]
	except:
		return _getText()
def get_product_blocks(url):
    page = re.get(URL)
    soup = bs(page.text,'html.parser')
    product_block = soup.find_all('div',{'class':'product-blocks'})
    products_section =  product_block[0]
    title3 = products_section.find_all('h3')
    print '\n'.join(['%s:%s'%(p.get_text(),try1([a for a in p.parent.children]).get_text()) for p in title3])
