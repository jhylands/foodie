from bs4 import BeautifulSoup as bs
from .ProductExtractor import ProductExtractor

class ItemNotFound(Exception):
    pass

class IcelandExtractor(ProductExtractor):
    def __init__(self,resp):
        self.soup = bs(resp,'html.parser')
        
    def getImage(self):
        images = self.soup.findAll('img',{'id':'zoom'})
        if images !=[]:
            return images[0]['src']
        else:
            raise ItemNotFound

    def getTitle(self):
        h1s = self.soup.findAll('h1')
        if h1s !=[]:
            return h1s[0].get_text()
        else:
            raise ItemNotFound

    def getPricePerUnit(self):
        priceContainers = self.soup.findAll('div',{'class':['detailPriceContainer']})
        if priceContainers!=[]:
            priceContainer = priceContainers[0]
            priceElement = priceContainer.findAll('span',class_=['big-price'])[0] #risk of exception
            price = self.getPrice(priceContainer.get_text())
            return price
        else:
            raise ItemNotFound

    def getPricePerMeasure(self):
        price, measure = self.getPriceWithMeasure()
        return price

    def getPricePerMeasureMeasure(self):
        price, measure = self.getPriceWithMeasure()
        return measure
        
    def getPriceWithMeasure(self):
        priceContainers = self.soup.findAll('div',{'class':['detailPriceContainer']})
        if priceContainers!=[]:
            priceContainer = priceContainers[0]
            priceElement = priceContainer.findAll('div')[0] #risk of exception
            return self.getPriceAndMeasure(priceElement.get_text())
        else:
            raise ItemNotFound

        

    def getInformation(self):
        info_containers = self.soup.findAll('div',{'id':'prod_tabs'})
        try:
            info_boxes = info_containers[0].findAll('div',class_=['prod_content'])
        except:
            return info_containers
        dicInformation = {}
        for info_box in info_boxes:
            try:
                section_title = info_box.findAll('h5')[0].get_text()
            except IndexError:
                section_title = 'InformationNoTitle'
            dicInformation.update({section_title:str(info_box)})
        return dicInformation
            
        
    '''
    function to output the feature of the page as a dictionary
    '''
    def toDictionary(self):
        #dictionayr to return 
        d = {}
        d.update(self.getInformation())
        d.update({'title':self.getTitle()})
        d.update({'pricePerUnit':self.getPricePerUnit()})
        d.update({'pricePerMeasure':self.getPricePerMeasure()})
        d.update({'pricePerMeasureMeasure':self.getPricePerMeasureMeasure()})
        return d

