#tesco box extractor

#main function that will be imported 

#soup - the whole page soup
def getDictionary(soup):
    dictProduct = {'Error':''}
    #find the container of all the sections
    text_sections = soup.find_all('div',class_='product-blocks')
    #if there are no text sections return the whole description
    if text_sections==[]:
        return self.getXML(soup)
    else:
        getBoxes(text_sections,dictProduct)
    return dictProduct


def getBoxes(boxes,dictProduct):
    #product description exists
    info_boxes = boxes[0].children
    for info_box in info_boxes:
        getBox(info_box,dictProduct)

def tryGetBoxTitle(box,d=1):
    if d==4:
        return False
    title = box.find_all('h%d'%d)
    if title==[]:
        return tryGetBoxTitle(box,d+1)
    else:
        return unicode(title[0].getText()).encode('utf-8')

'''
param soup (bs4 soup)
param dictProduct (dictionary by reference)
return void
'''    
def getBox(box,dictProduct):
    title = tryGetBoxTitle(box)
    if title and len(list(box.children))>1:
        dictProduct[title] =str( list(box.children) [1:])
    elif title:
        dictProduct[str(title)] = str(list(box))
    else:#there is no title 
        if 'untitled' in dictProduct:
            dictProduct['untitled']+=box.get_text()
        else:
            dictProduct['untitled'] = box.get_text()

def getXML(soup,dictProduct):
    info = soup.find_all('div',{'class':'product-blocks'})
    if info!=[]:
        description_title=info[0].find_all('h3')
        if description_title!=[]:
            if description_title[0].get_text()=='Description':
                return {'Description':info} 
        return {'XML':info}
    else:
        info = soup.find_all('div', class_='grocery-product__container')
        if info!=[]:
            return {'Description':info.get_text()}
        else:
            return {'Error':'No product info found'}
        
