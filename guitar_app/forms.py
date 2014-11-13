from django.forms import ModelForm, TextInput, Form, CharField, IntegerField, NullBooleanField
import models
from mongodbforms import EmbeddedDocumentForm
from mongodbforms import DocumentForm

"""class GuitarAddForm(ModelForm):
    class Meta:
        model = models.Guitars
        fields = '__all__'
        exclude = ['id']"""

class GuitarAddForm(Form):
    name = CharField(required=False)
    string_amount = IntegerField(required=False)
    price = IntegerField(required=False)
    neck_material = CharField(required=False)
    fretboard_material = CharField(required=False)
    pick_guard = NullBooleanField(required=False)
    type = CharField(required=False)
    body_material = CharField(required=False)
    body_color = CharField(required=False)
    body_type = CharField(required=False)
    body_form = CharField(required=False)


