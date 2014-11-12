from __future__ import unicode_literals

from django.db import models
from djangotoolbox.fields import EmbeddedModelField, ListField
from mongoengine import Document, StringField, IntField, BooleanField

class Producer(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    guitar = models.IntegerField(blank=True, default=0, null=True)
    bridge = models.IntegerField(blank=True, default=0, null=True)
    pickups = models.IntegerField(blank=True, default=0, null=True)
    info = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.name

class Body(models.Model):
    #id = models.IntegerField(primary_key=True)
    material = models.CharField(max_length=45, blank=True, null=True)
    color = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    form = models.CharField(max_length=45, blank=True, null=True)
    def __unicode__(self):
        return self.material

class Bridge(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    material = models.CharField(max_length=45, blank=True, null=True)
    color = models.CharField(max_length=45, blank=True, null=True)
    def __unicode__(self):
        return self.name

class Guitars(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, null=True)
    string_amount = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    neck_material = models.CharField(max_length=45, null=True)
    fretboard_material = models.CharField(max_length=45, null=True) # Field name made lowercase.
    pick_guard = models.NullBooleanField(null=True, default=False) # Field name made lowercase.
    type = models.CharField(max_length=45, null=True)
    body = EmbeddedModelField('Body', null=True)
    bridge = EmbeddedModelField('Bridge', null=True)
    pickups = EmbeddedModelField('Pickup', null=True)
    producer = EmbeddedModelField('Producer', null=True)

class Pickup(models.Model):
    #id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    set_type = models.CharField(max_length=45, blank=True, null=True)
    def __unicode__(self):
        return self.set_type
