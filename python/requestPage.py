import requests as re
import MySQLdb as sql

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
        return f.read().decode('utf8')

def fetchFromServer(URL):
    headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    #The next line should be considered sacrid only run when absolutly needed
    r = re.get(URL,headers = headers)
    #would be better to have a db connection
    store(URL,r.text)

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
