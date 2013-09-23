# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import sys

#establish a db connection
conn = MongoClient("localhost", 27017)

#get a handle o the school db & grades collection
db = conn.students
grade = db.grades

query = {'type':'homework'}

try:
  cur = grade.find(query).sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])
  for idx, doc in enumerate(cur):
    if idx % 2 == 0:
      #print doc
      db.grades.remove({'_id':doc['_id']})
except:
  "Unexpected error", sys.exc_info()[0]  

