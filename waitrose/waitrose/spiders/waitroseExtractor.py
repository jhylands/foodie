
from pyvirtualdisplay import Display
from selenium import webdriver
display = Display(visible=0, size=(800, 600))
display.start()
from .ProductExtractor import ProductExtractor

class ItemNotFound(Exception):
    pass

class WaitroseExtractor(ProductExtractor):
    def __init__(self,url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        
    def getImage(self):
        image_container =self.driver.find_element_by_class_name("detailsContainer___1x_EW")
        image = image_container.find_element_by_tag_name("img")
        return image.get_attribute('src')

    def getTitle(self):
        title =self.driver.find_element_by_class_name("name___30fwb")
        return title.text

    def getPricePerUnit(self):
        price_container = self.driver.find_element_by_class_name("productPricing___1GkLr")
        price_spans = price_container.find_elements_by_tag_name("span")
        return self.getPrice(price_spans[1].text)

    def getPricePerMeasure(self):
        price, measure = self.getPriceWithMeasure()
        return price

    def getPricePerMeasureMeasure(self):
        price, measure = self.getPriceWithMeasure()
        return measure
        
    def getPriceWithMeasure(self):
        price_container = self.driver.find_element_by_class_name("productPricing___1GkLr")
        price_spans = price_container.find_elements_by_tag_name("span")
        return self.getPriceAndMeasure(price_spans[2].text[1:-1]) #[1:-1] to get rid of the brackets

    

    def getIngredients(self):
        return self.waitroseDescBox("accordioningredients","ingredients___3hZlR")
    def getNutrition(self):
        return self.waitroseDescBox("accordionnutrition","nutrition___24-Nx")
    def getProductDetails(self):
        return self.waitroseDescBox("accordionproductDetails","body___nJ3yf")

    def waitroseDescBox(self,head_id,inner_class):
        ingre = self.driver.find_element_by_id(head_id)
        ingre_inner = self.driver.find_element_by_class_name(inner_class)
        if ingre_inner.text=='':
            ingre.click()
            if ingre_inner.text=='':
                ingre.click()
        return ingre_inner.text 

            
        
    '''
    function to output the feature of the page as a dictionary
    '''
    def toDictionary(self):
        #dictionayr to return 
        d = {}
        d.update({'Ingredients':self.getIngredients()})
        d.update({'Nutrition':self.getNutrition()})
        d.update({'Product Details':self.getProductDetails()})
        d.update({'title':self.getTitle()})
        d.update({'pricePerUnit':self.getPricePerUnit()})
        d.update({'pricePerMeasure':self.getPricePerMeasure()})
        d.update({'pricePerMeasureMeasure':self.getPricePerMeasureMeasure()})
        return d

