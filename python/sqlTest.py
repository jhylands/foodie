#!/usr/bin/python

import MySQLdb as sql

# Open database connection
db = sql.connect("timep.co.uk","timepcou_food","foodiseverything","timepcou_food" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print "Database version : %s " % data

# disconnect from server
db.close()
