import requests as re
import MySQLdb as sql

def getAssignment(a):
    #db =  sql.connect("timep.co.uk","timepcou_food","foodiseverything","timepcou_food" )
    db =  sql.connect("localhost","root","space(176)","timepcou_food" )
    cursor = db.cursor()
    cursor.execute("SELECT * from Links Where Expanded=0")
    results = cursor.fetchall()
    URL=0
    ID=0
    ID=results[a][0]
    URL=results[a][1]
    assert(ID!=0)
    cursor.execute("UPDATE Links SET Expanded = 1 Where LinkID=%s",(ID,))
    cursor.close()
    assert(URL!=0)
    return URL
import warnings
warnings.filterwarnings('ignore', category=sql.Warning)
def postLinks(links):
    #db =  sql.connect("timep.co.uk","timepcou_food","foodiseverything","timepcou_food" )
    db =  sql.connect("localhost","root","space(176)","timepcou_food" )
    db.set_character_set('utf8')
    cursor = db.cursor()
    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')
    cursor.executemany("Insert IGNORE INTO Links (Link,Expanded) Values (%s,0)",[(link,) for link in links])


def checkCache(URL):
    db =  sql.connect("timep.co.uk","timepcou_food","foodiseverything","timepcou_food" )
    cursor = db.cursor()
    cursor.execute("SELECT * from pageCache Where URL=%s",(URL,))
    results = cursor.fetchall()
    ID=0
    for row in results:
        ID=row[0]
    cursor.close()
    return ID

def fetchFromFile(ID):
    with open('../cache/'+str(ID),'r') as f:
        return f.read()#.decode('utf8')

def fetchFromServer(URL):
    headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    #The next line should be considered sacrid only run when absolutly needed
    r = re.get(URL,headers = headers)
    #would be better to have a db connection
    assert(r.text!=None)
    store(URL,r.text)
    return r.text

def dbStore(URL):
    db =  sql.connect("timep.co.uk","timepcou_food","foodiseverything","timepcou_food" )
    cursor = db.cursor()
    cursor.execute("insert into pageCache (URL) values(%s)",(URL,))
    cursor.close()
    return cursor.lastrowid


def fileStore(ID,HTML):
    with open('../cache/'+str(ID),'wb') as f:
        f.write(HTML.encode('utf8'))

def store(URL,HTML):
    assert(HTML!=None)
    ID = dbStore(URL)
    fileStore(ID,HTML)


def getAsString(URL):
    ID = checkCache(URL)
    if ID==0 :
        return fetchFromServer(URL)
    else:
        return fetchFromFile(ID)

# prepare a cursor object using cursor() method

# execute SQL query using execute() method.
# Fetch a single row using fetchone() method.

# disconnect from server
#def get(URL):
#    return parse(getAsString(URL))
