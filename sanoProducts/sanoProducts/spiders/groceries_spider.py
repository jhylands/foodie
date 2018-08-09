import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor as getLinks
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector 
#from html2text import html2text as html2txt
from bs4 import BeautifulSoup as bs

class GrocerySpider(scrapy.Spider):
    name='groceries'
    allowed_domains =['https://sainsburys.co.uk','sainsburys.co.uk']
    start_urls =  ['https://www.sainsburys.co.uk/shop/gb/groceries/']

    
    def parse(self,response):
        productpage = response.css('div.productTitleDescriptionContainer').extract() 
        if not productpage:
#allow='\/groceries\/'
            links = getLinks(allow='\/groceries\/').extract_links(response)
            for link in links:
                yield scrapy.Request(link.url, callback=self.parse)
        else:
            yield self.gatherProduct(response)

    def gatherProduct(self,response):
        dictProduct = self.gatherProductBS(response)
        
        #Streamlined respose CSS selector (SCSS)
        def scss(selector):
            return response.css(selector).extract()
        dictProduct['title'] = scss('div.productTitleDescriptionContainer h1::text')
        dictProduct['img'] = scss('div#productImageHolder img::attr(src)')
        dictProduct['pricePU'] = scss('p.pricePerUnit::text')
        dictProduct['pricePM'] =scss('p.pricePerMeasure::text')
        
        return dictProduct

    #gather the product information using beautiful soup
    def gatherProductBS(self,response):
        dictProduct = {'Error':''}
        soup = bs(response.text,'html.parser')
        text_sections = soup.find_all('div',class_=['productText'])
        if text_sections[0].find_all('h3') == []:
            #sano product
            text_titles = [title.get_text() for title in soup.find_all('h3',class_=['productDataItemHeader'])]
            product_pair = zip(text_titles,text_sections)
            for title,desc in product_pair:
                dictProduct[title] = desc
        else:
            #branded product
            for text_section in text_sections:
                try:
                    title = text_section.find_all('h3')[0].get_text() #could throw error
                    desc = text_section
                    dictProduct[title] = desc
                except:
                    #if there is a problem with adding the information in a granular format add it in a more structured format
                    dictProduct['Error'] += str(text_section)

        return dictProduct
        #.select('//div[@class="itemTypeGroupContainer productText"]/h3[text()]').extract()
