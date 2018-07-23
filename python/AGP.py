#AGP.py
# a program that gets the Assignment (an unexpanded link)
#expands the link by Getting the page
#Processes that page probably generating new links to expand
from requestPage import getAsString,getAssignment, postLinks
from getLinks import getLinks
import _thread
import time
def main(a):
    print (a)
    URL = getAssignment(a)
    print ("Target aquired:")
    print (URL)
    raw_html = getAsString(URL)
    print ("Page retrived")
    links = getLinks(raw_html,URL)
    print ("%d links found adding them now"%(len(links)))
    postLinks(links)
    print ("Assignment complete")
def mainL(a):
    for i in range(100):
        print ("i:%d"%i)
        main(a)
for x in range(64):
    _thread.start_new_thread(mainL,(x,))
    print ("Job: %d"%(x))
    time.sleep(.5)
input()
