from django.db import models

# Create your models here.
import datetime
 
# Create your models here.
 
 
class Product(models.Model):
 
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
 
    def __unicode__(self):
        return self.name
 
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'desc': self.description,
            'price': self.price,
            'date_created': self.date_created,
            'date_modified': self.date_modified
        }
