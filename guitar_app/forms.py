from django.forms import ModelForm, TextInput, Form, CharField, IntegerField, NullBooleanField
import models
from mongodbforms import EmbeddedDocumentForm
from mongodbforms import DocumentForm

class GuitarAddForm(ModelForm):
    class Meta:
        model = models.Guitars
        fields = '__all__'
        exclude = ['id']

"""class GuitarAddForm(ModelForm):
    name = CharField(required=False)
    string_amount = IntegerField(required=False)
    price = IntegerField(required=False)
    neck_material = CharField(required=False)
    fretboard_material = CharField(required=False)
    pick_guard = NullBooleanField(required=False)
    type = CharField(required=False)
    body_material = CharField(required=False, label="material")
    body_color = CharField(required=False, label="color")
    body_type = CharField(required=False, label="type")
    body_form = CharField(required=False, label="form")
    producer_name = CharField(required=False, label='name')
    producer_rating = IntegerField(required=False, label='rating')
    producer_info = CharField(required=False, label='info')
    bridge_name = CharField(required=False, label='name')
    bridge_material = CharField(required=False, label='material')
    bridge_color = CharField(required=False, label='color')
    pickup_type = CharField(required=False, label='type')
    pickup_set_type = CharField(required=False, label='set type')"""



