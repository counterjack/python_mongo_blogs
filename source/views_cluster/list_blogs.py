# create views here

import pymongo
from pymongo import MongoClient
#from base_settings.settings import DATABASE_SETTINGS
from constants import *

client = MongoClient(port=27017)
db = client.blogs
collection = db.post

def list_view(page_number=0):
    collec = db.post

    blogs = []
    all_blogs = collec.find()
    for blog in all_blogs:
        blogs.append(blog)
    print blogs
    print "Total blogs fetched : {}".format(len(blogs))
    print  "Blog with maximum liked :{}".format(1)
    print "Happy Blogging !!"
    return blogs

if __name__ == '__main__':
    list_view()




