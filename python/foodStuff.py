'''
Does add mean, to mix the two products together?
'''


#This represents an ammount of a single food stuff
class FoodStuff:
    def __init__(productId,ammount):
        self.productId = productId
        self.ammount = ammount
        
    def getShelfLife(self):
        pass
    
    #should this function mutate self?
    def __add__(self,product):
        #depending on what the other product is
        if product.getId()==self.getId():
            self.ammount += product.ammount
            #merge shelf life etc
        elif product.superclass()==self.superclass():
            pass
        return self
    
    def __iadd__(self,product):
        self = self + product
    def __sub__(self,product):
        pass

    
class mixedFoodStuff:
    def __init__(component):
        self.components = [component]
    
    #this is dissimilar to (+) because it is adding another product to the mixture
    def add(self,foodStuff):
        self.components = [component]
        
    def __add__(self,product):
        #this has seperate semantics to .add() because this is closer to an arithmetic add
        pass
