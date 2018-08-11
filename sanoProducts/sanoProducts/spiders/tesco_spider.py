# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor as getLinks
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector 
#from html2text import html2text as html2txt
from bs4 import BeautifulSoup as bs
import re as reg

class GrocerySpider(scrapy.Spider):
    name='tesco'
    allowed_domains =['https://tesco.co.uk','tesco.co.uk']
    start_urls =  ['https://www.sainsburys.co.uk/shop/gb/groceries/']

    
    def parse(self,response):
        productpage = response.css('div.product-title__h1').extract() 
        if not productpage:
#allow='\/groceries\/'
            links = getLinks(allow='\/groceries\/').extract_links(response)
            for link in links:
                yield scrapy.Request(link.url, callback=self.parse)
        else:
            yield self.gatherProduct(response)

    def gatherProduct(self,response):
        soup = bs(response.text,'html.parser')
        dictProduct = self.gatherProductBS(soup)
        
        #Streamlined respose CSS selector (SCSS)
        def scss(selector):
            return response.css(selector).extract()
        dictProduct['title'] = scss('div.product-title__h1 h1::text')[0]
        dictProduct['img'] = scss('div.product-image__container img::attr(src)')[0]
        
        #get price information, add it to the dictionary
        #source:https://stackoverflow.com/questions/38987/how-to-merge-two-dictionaries-in-a-single-expression
        dictProduct.update(self.getPrice(soup))

        return dictProduct

    #gather the product information using beautiful soup
    def gatherProductBS(self,soup):
        dictProduct = {'Error':''}
        text_sections = soup.find_all('div',class_=['product-blocks'])
        if text_sections==[]:
            return self.getXML(soup)
        else:
            #product description exists
            info_boxes = text_sections[0].children
            for info_box in info_boxes:
                title = info_box.find_all('h3')[0].get_text()
                if len(info_box.children)>1:
                    desc = info_box.children[1:]
                else:
                    desc = info_box
                dictProduct[title] = desc
        return dictProduct



    def getPrice(self, soup):
        price_group = soup.find_all('div',class_='price-details--wrapper')
        if price_group == []:
            return {'price':'no price group'}#escape in no price group
        PPU = price_group[0].find_all('p',class_='price-control-wrapper')[0].get_text()
        PPM = price_group[0].find_all('p',class_='price-per-quantity-weight')[0].get_text()
#        try:
        PPU_group = reg.search(ur'£(\d+\.\d{2})\/(\w+)',PPU,flags=reg.UNICODE)
        
        price_per_unit = PPU_group.group(1)
        price_per_unit_unit = PPU_group.group(2)
        PPM_group = reg.search(ur'£(\d+\.\d{2})\/(\w+)',PPM,flags=reg.UNICODE)
        price_per_measure = PPM_group.group(1)
        price_per_measure_measure = PPM_group.group(2)
        return {'pricePerUnit':price_per_unit,
                'pricePerUnitUnit':price_per_unit_unit,
                'PricePerMeasure':price_per_measure,
        'PricePerMeasureMeasure':price_per_measure_measure}
#        except Exception as ex:
 #           return{'price': 'PPU:%s;{PPU:%s,\nPPM:%s}'%(ex.message,PPU,PPM)} 

    def getXML(self,soup):
        info = soup.find_all('div',{'class':'product-blocks'})[0]
        description_title=info.find_all('h3')
        if description_title!=[]:
            if description_title[0].get_text()=='Description':
                return {'Description':info} 
        return {'XML':info}
        
        
