# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider
from .waitroseExtractor import WaitroseExtractor
from selenium.common.exceptions import NoSuchElementException

class ProductsSpider(SitemapSpider):
    name = 'products'
    sitemap_urls = ['https://www.waitrose.com/content/waitrose/en/public/xmlsitemap/sitemap0.xml']

    def parse(self, response):
        e = WaitroseExtractor(response.url)
        try:
            return e.toDictionary()
        except NoSuchElementException:
                print ("Error on page")

        
