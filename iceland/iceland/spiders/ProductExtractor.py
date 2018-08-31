import re
class NoPrice(Exception):
    pass
class NoMeasure(Exception):
    pass

class ProductExtractor():
    '''
    Function to extract prices from some text (prices in UK currency)
    param str text
    return [float] prices
    '''
    def getPrice(self,text):
        price_group = re.search("(?:£(\d+\.\d{2}))|(?:(\d+)p)",text,flags=re.UNICODE)
        if price_group.group(1):
            price = float(price_group.group(1))
        elif price_group.group(2):
            price = float(price_group.group(2))/100
        else:
            raise NoPrice
        return price
    '''
    function to extract the price and mesure information from text
    param str text
    return (float,str) (the price, the units of the per measure
    '''
    def getPriceAndMeasure(self,text):
        price_group = re.search("(?:(?:£(\d+\.\d{2}))|(?:(\d+)p))\s?(?:\/|per)\s?(\d+\s\w+|\w+)",text,flags=re.UNICODE)
        if price_group.group(1):
            price = float(price_group.group(1))
        elif price_group.group(2):
            price = float(price_group.group(2))/100
        else:
            raise NoPrice
        if price_group.group(3):
            price_per_measure_measure = price_group.group(3)
        else:
            raise NoMeasure
        return (price,
                price_per_measure_measure)
    
    
