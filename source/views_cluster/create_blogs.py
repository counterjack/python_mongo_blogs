# create views here

import pymongo
from pymongo import MongoClient
#from base_settings.settings import DATABASE_SETTINGS
#from constants import *
from constants import BLOG_POST_FIELDS

client = MongoClient(port=27017)
db = client.blogs
collection = db.post

def create_view(page_number=0):
    collec = db.post
    blogs = []
    for item in BLOG_POST_FIELDS:
        if not isinstance(item, list):
            BLOG_POST_FIELDS[item] = input('Please insert {} : '.format(item))
        else:
            for subitem in item:
                BLOG_POST_FIELDS[item][subitem] = input('Please insert {} : '.format(subitem))

    print BLOG_POST_FIELDS
    collec.insert(BLOG_POST_FIELDS)
    print blogs
    return blogs

if __name__ == '__main__':
    create_view()




