from __future__ import unicode_literals

from django.db import models
from djangotoolbox.fields import EmbeddedModelField, ListField
from mongoengine import Document, StringField, IntField, BooleanField

class Guitars(models.Model):
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