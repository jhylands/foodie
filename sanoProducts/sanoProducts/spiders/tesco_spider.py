# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor as getLinks
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector 
#from html2text import html2text as html2txt
from bs4 import BeautifulSoup as bs
import re as reg
from boxEx.tesco import getDictionary

class GrocerySpider(scrapy.Spider):
    name='tesco'
    allowed_domains =['tesco.co.uk','www.tesco.co.uk','www.tesco.com','tesco.com']
    start_urls =  ['https://www.tesco.com/groceries/en-GB/products/292276301','https://www.tesco.com/groceries/']

    
    def parse(self,response):
        productpage = response.css('h1.product-title__h1').extract() 
        if not productpage:
#allow='\/groceries\/'
            links = getLinks(allow=['\/groceries\/','/^.{9,200}$/']).extract_links(response)
            for link in links:
                yield scrapy.Request(link.url, callback=self.parse)
        else:
            yield self.gatherProduct(response)

    def gatherProduct(self,response):
        soup = bs(response.text,'html.parser')
        dictProduct = getDictionary(soup)
        
        #Streamlined respose CSS selector (SCSS)
        def scss(selector):
            return response.css(selector).extract()
        dictProduct['title'] = self.getTitle(soup)
        dictProduct['img'] = scss('div.product-image__container img::attr(src)')[0]
        
        #get price information, add it to the dictionary
        #source:https://stackoverflow.com/questions/38987/how-to-merge-two-dictionaries-in-a-single-expression
        dictProduct.update(self.getPrice(soup))

        return dictProduct
    def getTitle(self,soup):
        title = soup.find_all('h1',class_='product-title__h1')
        if title !=[]:
            return title[0].get_text()
        else:
            return 'Unknown'

    def getPrice(self, soup):
        price_group = soup.find_all('div',class_='price-details--wrapper')
        if price_group == []:
            return {'price':'no price group'}#escape in no price group
        PPU = price_group[0].find_all('div',class_='price-control-wrapper')[0].get_text()
        PPM = price_group[0].find_all('div',class_='price-per-quantity-weight')[0].get_text()
        try:
           PPU_group = reg.search(ur'£\s?(\d+\.\d{2})',PPU,flags=reg.UNICODE)
           
           price_per_unit = PPU_group.group(1)
           #price_per_unit_unit = PPU_group.group(2)
           PPM_group = reg.search(ur'£(\d+\.\d{2})\/(\w+)',PPM,flags=reg.UNICODE)
           price_per_measure = PPM_group.group(1)
           price_per_measure_measure = PPM_group.group(2)
           return {'pricePerUnit':price_per_unit,
                   #'pricePerUnitUnit':price_per_unit_unit,
                   'PricePerMeasure':price_per_measure,
           'PricePerMeasureMeasure':price_per_measure_measure}
        except Exception as ex:
            return{'price': 'PPU:%s;{PPU:%s,\nPPM:%s}'%(ex.message,PPU,PPM)} 

        
        
