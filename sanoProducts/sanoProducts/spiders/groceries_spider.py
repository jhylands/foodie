import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor as getLinks
from scrapy.linkextractors import LinkExtractor


class GrocerySpider(scrapy.Spider):
    name='groceries'
    allowed_domains =['https://sainsburys.co.uk','sainsburys.co.uk']
    start_urls =  ['https://www.sainsburys.co.uk/shop/gb/groceries/']

    def parse(self,response):
        productpage = response.css('div.productTitleDescriptionContainer h1::text').extract() 
        if not productpage:
#allow='\/groceries\/'
            links = getLinks().extract_links(response)
            for link in links:
                yield scrapy.Request(link.url, callback=self.parse)
        
        yield {'content':productpage}

