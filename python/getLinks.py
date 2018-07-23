from bs4 import BeautifulSoup as bs

#function to remove any within page links, #top ect

def removeHashtag(link):
    val = link.find('#')
    if val==-1:
        return link
    else:
        return link[:val]

def getLinks(raw_html,base):
    soup = bs(raw_html,'html.parser')
    all_a = soup.find_all('a')
    def tryGetHref(a):
        try:
            return a['href']
        except:
            return None
    links_from_a = map(tryGetHref,all_a)
    links_from_a = [a for a in links_from_a if a is not None]
    def addBase(link):
        if link[:4] != 'http':
            link = base + link
        return link
    return [addBase(removeHashtag(a)) for a in links_from_a]


