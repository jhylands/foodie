# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
def tryString(string):
    try:
        return str(string)
    except UnicodeEncodeError:
        return unicode(string)

class icelandPipeline(object):
    def open_spider(self,spider):
        self.file = open('output.json','w')
        self.file.write('[')
        self.cache = []

    def close_spider(self,spider):
        #pickle.dump(self.cache,self.file)
        #self.file.write(json.dumps(self.cache))
        self.file.close()
        with open('output.json','rb+') as f:
            f.seek(-2,os.SEEK_END)
            f.truncate()
        
        with open('output.json','a') as f:
            f.write(']')

    def process_item(self, item, spider):
        storeDic = {}
        for key in item:
            storeDic[key] = tryString(item[key])
        self.file.write(json.dumps(storeDic) + ',\n')
        #self.file.write("{%s}"%'\n'.join(["%s:%s,\n"%(key,str(item[key])) for key in list(item.keys())]))
        #self.file.write(',')
        #self.cache.append(storeDic)
        return item
