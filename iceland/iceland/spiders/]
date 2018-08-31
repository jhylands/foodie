# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider
from .icelandExtractor import IcelandExtractor
class ProductsSpider(SitemapSpider):
    name = 'products'
    sitemap_urls = ['https://groceries.iceland.co.uk/assets/sitemap-products.xml']

    def parse(self, response):
        e = IcelandExtractor(response.text)
        return e.toDictionary()
        
