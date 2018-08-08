import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class GrocerySpider(CrawlSpider):
    name='groceries'
    allowed_domains =['https://sainsburys.co.uk']
    start_urls =  ['https://www.sainsburys.co.uk/shop/gb/groceries/']
    rules = (Rule(LinkExtractor(allow='\/groceries\/'),callback='parse'),)

    def parse(self,resposne):
        pass

