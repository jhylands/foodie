# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os

class SanoproductsPipeline(object):
    def open_spider(self,spider):
        self.file = open('output.james','w')
        self.file.write('[')
        self.cache = []

    def close_spider(self,spider):
        #pickle.dump(self.cache,self.file)
        #self.file.write(json.dumps(self.cache))
        self.file.close()
        with open('output.james','rb+') as f:
            f.seek(-2,os.SEEK_END)
            f.truncate()
        
        with open('output.james','a') as f:
            f.write(']')

    def process_item(self, item, spider):
        storeDic = {}
        for key in item:
            storeDic[key] = str(item[key])
        self.file.write(json.dumps(storeDic) + ',\n')
        #self.file.write("{%s}"%'\n'.join(["%s:%s,\n"%(key,str(item[key])) for key in list(item.keys())]))
        #self.file.write(',')
        #self.cache.append(storeDic)
        return item
