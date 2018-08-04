from mongoengine import (Document, EmbeddedDocument,
                         DynamicDocument
                         )
from mongoengine.fields import *
import datetime


class BlogPost(DynamicDocument):
    """
        defines schema of Post Collection
    """
    user = StringField(required=True, db_field='by_user')
    description = StringField(required=True)
    tags = ListField(StringField())
    comments = ListField(DictField())
    url = URLField()
    title = StringField(required=True)
    likes = IntField(default=0)
    date_created = DateTimeField(default=datetime.datetime.utcnow)
    date_updated = DateTimeField(default=datetime.datetime.utcnow)

    def save(*args, **kwargs):
        self.date_updated = datetime.datetime.utcnow
        super(self, BlogPost).save(*args, **kwargs)





#class Comments()






