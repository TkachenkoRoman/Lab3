from __future__ import unicode_literals
from django.db import models
from djangotoolbox.fields import EmbeddedModelField, ListField
from mongoengine import Document, StringField, IntField, BooleanField
from django_mongodb_engine.contrib import MongoDBManager

class Guitars(models.Model):
    objects = MongoDBManager()
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    string_amount = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    neck_material = models.CharField(max_length=45,blank=True, null=True)
    fretboard_material = models.CharField(max_length=45,blank=True, null=True) # Field name made lowercase.
    pick_guard = models.NullBooleanField(blank=True, null=True, default=False) # Field name made lowercase.
    type = models.CharField(max_length=45,blank=True, null=True)
    #body = EmbeddedModelField('Body', null=True)
    #bridge = EmbeddedModelField('Bridge', null=True)
    #pickups = EmbeddedModelField('Pickup', null=True)
    #producer = EmbeddedModelField('Producer', null=True)
    producer_name = models.CharField(max_length=45, blank=True, null=True)
    producer_rating = models.IntegerField(blank=True, null=True)
    producer_info = models.TextField(blank=True, null=True)
    body_material = models.CharField(max_length=45, blank=True, null=True)
    body_color = models.CharField(max_length=45, blank=True, null=True)
    body_type = models.CharField(max_length=45, blank=True, null=True)
    body_form = models.CharField(max_length=45, blank=True, null=True)
    bridge_name = models.CharField(max_length=45, blank=True, null=True)
    bridge_material = models.CharField(max_length=45, blank=True, null=True)
    bridge_color = models.CharField(max_length=45, blank=True, null=True)
    pickup_type = models.CharField(max_length=45, blank=True, null=True)
    pickup_set_type = models.CharField(max_length=45, blank=True, null=True)

#class Statistics(models.Model):
#    _id = models.CharField(max_length=45, blank=True, null=True)
#    value = models.IntegerField(blank=True, null=True)

map_guitar_types = """
                    function() {
                    emit(this.type, {count: 1});
                    };"""

reduce_guitar_types = """function reduce(key, values) {
                         var sum = 0;
                         values.forEach(function(value){
                            sum += value['count'];
                         });
                         return {count: sum};
                         };"""

map_guitar_price = """function() {
                    Value = {price: this.price, low_price: 0, middle_price: 0, high_price: 0}
                    if (Value.price <= 500)
                    {
                        Value.low_price = 1;
                    }
                    if (Value.price > 500 && Value.price <= 2000)
                    {
                        Value.middle_price = 1;
                    }
                    if (Value.price > 2000)
                    {
                        Value.high_price = 1;
                    }
                    emit(this.producer_name, Value);
                    };"""

reduce_guitar_price = """function reduce_prices(key, values) {
                         reducedValue = {price: 0, low_price: 0, middle_price: 0, high_price: 0}
                         values.forEach(function(value){
                            if (value['price'] <= 500)
                            {
                                reducedValue.low_price += 1;
                            }
                            if (value['price'] > 500 && value['price'] <= 2000)
                            {
                                reducedValue.middle_price += 1;
                            }
                            if (value['price'] > 2000)
                            {
                                reducedValue.high_price += 1;
                            }
                         });
                         return reducedValue;
                         };"""