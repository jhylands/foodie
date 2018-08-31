# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider
from .aldiExtractor import AldiExtractor
class ProductsSpider(SitemapSpider):
    name = 'products'
    sitemap_urls = ['https://www.aldi.co.uk/sitemap/product']

    def parse(self, response):
        e = AldiExtractor(response.text)
        try:
            return e.toDictionary()
        except:
            print('Error scraping page')
