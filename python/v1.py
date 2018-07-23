from bs4 import BeautifulSoup as bs


def getLinks(raw_html,base):
    soup = bs(raw_html,'html.parser')
    links_from_a = map(lambda x:x['href'],soup.find_all('a'))
    def addBase(link):
        if link[:7] != 'http://':
            link = base + link
        return link
    return map(addBase, links_from_a)


