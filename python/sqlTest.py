#!/usr/bin/python

import MySQLdb as sql

# Open database connection
db = sql.connect("timep.co.uk","timepcou_food","foodiseverything","timepcou_food" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

url ='www.bbcgoodfood.com'
cursor.execute("insert into pageCache (URL) values(%s)",(url,))
print cursor.lastrowid
# execute SQL query using execute() method.
cursor.execute("SELECT * from pageCache Where URL=%s",(url,))
results = cursor.fetchall()
for row in results:
    ID=row[0]
# Fetch a single row using fetchone() method.
print "Database version : %s " % ID

# disconnect from server
db.close()
