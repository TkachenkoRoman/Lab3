from django.forms import ModelForm, TextInput
import models
from mongodbforms import EmbeddedDocumentForm
from mongodbforms import DocumentForm

class GuitarAddForm(ModelForm):
    class Meta:
        model = models.Guitars
        fields = '__all__'
        exclude = ['id']

"""class GuitarAddForm(DocumentForm):
    class Meta:
        model = models.Guitars
        #embedded_field_name = 'body'
        fields = '__all__'
        exclude = ['id']"""
