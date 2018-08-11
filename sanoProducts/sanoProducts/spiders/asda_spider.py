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
    name='groceries'
    allowed_domains =['https://asda.co.uk','asda.co.uk']
    start_urls =  ['https://www.sainsburys.co.uk/shop/gb/groceries/','https://www.sainsburys.co.uk/shop/gb/groceries/sellotape-original-gold-24-x-50']

    
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
        soup = bs(response.text,'html.parser')
        dictProduct = self.gatherProductBS(soup)
        
        #Streamlined respose CSS selector (SCSS)
        def scss(selector):
            return response.css(selector).extract()
        dictProduct['title'] = scss('div.productTitleDescriptionContainer h1::text')[0]
        dictProduct['img'] = scss('div#productImageHolder img::attr(src)')[0]
        
        #get price information, add it to the dictionary
        #source:https://stackoverflow.com/questions/38987/how-to-merge-two-dictionaries-in-a-single-expression
        dictProduct.update(self.getPrice(soup))

        return dictProduct

    #gather the product information using beautiful soup
    def gatherProductBS(self,soup):
        dictProduct = {'Error':''}
        text_sections = soup.find_all('div',class_=['productText'])
        if text_sections==[]:
            return self.getXML(soup)
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



    def getPrice(self, soup):
        price_group = soup.find_all('div',class_='pricing')
        if price_group == []:
            return {'price':'no price group'}#escape in no price group
        PPU = price_group[0].find_all('p',class_='pricePerUnit')[0].get_text()
        PPM = price_group[0].find_all('p',class_='pricePerMeasure')[0].get_text()
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
        info = soup.find_all('div',{'id':'information'})[0]
        description_title=info.find_all('h3')
        if description_title!=[]:
            if description_title[0].get_text()=='Description':
                return {'Description':info} 
        return {'XML':info}
        
        
