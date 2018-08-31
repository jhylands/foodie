from .ProductExtractor import ProductExtractor
from bs4 import BeautifulSoup as bs

class ItemNotFound(Exception):
    pass

class AldiExtractor(ProductExtractor):
    def __init__(self,resp):
        self.soup = bs(resp,'html.parser')
        
    def getImage(self):
        picture = self.soup.findAll('picture')[0]
        
        images = picture.findAll('img')
        if images !=[]:
            return images[0]['src']
        else:
            raise ItemNotFound

    def getTitle(self):
        h1s = self.soup.findAll('h1',class_='product-details__name')
        if h1s !=[]:
            return h1s[0].get_text()
        else:
            raise ItemNotFound

    def getPricePerUnit(self):
        priceContainers = self.soup.findAll('li',{'class':['product-price__main']})
        if priceContainers!=[]:
            price = self.getPrice(priceContainers[0].get_text())
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
        priceContainers = self.soup.findAll('li',{'class':['product-price__detail']})
        if priceContainers!=[]:
            return self.getPriceAndMeasure(priceContainers[0].get_text())
        else:
            raise ItemNotFound

        

    def getInformation(self):
        info_containers = self.soup.findAll('div',{'class':'product-description__text'})
        return {'Product Information':info_containers[0].get_text()}
        
    '''
    function to output the feature of the page as a dictionary
    '''
    def toDictionary(self):
        #dictionayr to return 
        d = {}
        d.update(self.getInformation())
        d.update({'title':self.getTitle()})
        d.update({'pricePerUnit':self.getPricePerUnit()})
        try:
            d.update({'pricePerMeasure':self.getPricePerMeasure()})
            d.update({'pricePerMeasureMeasure':self.getPricePerMeasureMeasure()})
        except ItemNotFound:
            print('Not split item price')
        except AttributeError:
            print('Not split item price')
        return d
    
