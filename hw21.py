# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import sys

#establish a db connection
conn = MongoClient("localhost", 27017)

#get a handle o the school db & collection
db = conn.students
grade = db.grades

query = {'type':'exam', 'score': {'$gte':65}}

try:
  cur = grade.find(query).sort('score', pymongo.ASCENDING).limit(1)
except:
  print "Something went wrong: ", sys.exc_info()[0]

print "Sorting ascending so our first doc/row should be our match, only printing first doc\n"

for doc in cur:
  print doc
