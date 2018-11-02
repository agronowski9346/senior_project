from django.db import models

# Create your models here.
import datetime
 
# Create your models here.
class User(models.Model):
    username = models.TextField(blank=True, primary_key=True)
    email = models.TextField(null=True, blank=True)
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    password = models.TextField(null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True)
    home_address = models.TextField(null=True, blank=True)

class Location(models.Model):   
    location_name = models.TextField(blank=True, primary_key=True)
    address = models.TextField(null=True, blank=True)
    owner = models.TextField(null=True, blank=True)
    max_attendees = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)


class Event(models.Model):
    location_name = models.ForeignKey(Location, on_delete = models.CASCADE)
    address = models.TextField(blank=True, primary_key=True)
    location_name = models.TextField(null=True, blank=True)
    date_of_event = models.DateTimeField(auto_now_add=False, blank=True)
    owner = models.TextField(null=True, blank=True)
    unique_link = models.TextField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)


class Vendor(models.Model):
    company_name = models.TextField(blank=True, primary_key=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    description = models.TextField(null=True, blank=True)

class VendorData(models.Model):
    company_name = models.ForeignKey(Vendor, on_delete = models.CASCADE)
    # the events the vendor can provide services for
    events_types_serviced = models.TextField(null=True, blank=True)
    #services the vendor offers
    #like cake, dresses, makeup, dressing up
    services_offered = models.TextField(null=True, blank=True)

#represents more information about each Location 
#such as the pictures and dates a location is booked from
class LocationData(models.Model):
    location_name = models.ForeignKey(Location, on_delete = models.CASCADE)
    date = models.DateTimeField(default = None, null=True, blank=True)
    pictures = models.TextField(null=True, blank=True)
    event_types_sponsored = models.TextField(null=True, blank=True)
 
'''
sample model with its JSON representation
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
'''


