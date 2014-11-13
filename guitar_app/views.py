from django.shortcuts import render
from guitar_app import tables, models
from models import Guitars
from django_tables2   import RequestConfig
from django.http import HttpResponse, HttpResponseRedirect
from forms import *
from django.db.models import Max

def index(request):
    table = tables.GuitarTable(models.Guitars.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'guitar_app/index.html', {'table': table})

def guitar_detail(request, pk):
    return HttpResponse('guitar detail id= ' + pk)

def action(request):
    return HttpResponse('action')

def add(request):
    if request.method == 'POST':
        form = GuitarAddForm(request.POST)
        if form.is_valid():
            max_id = None
            if models.Guitars.objects.all():
                max_id = models.Guitars.objects.order_by('-id')[0].id #order by desc, get first elem id
            if not max_id:
                max_id = 0
            guitar = models.Guitars.objects.create(id=int(max_id)+1,
                                                   name=form.cleaned_data['name'],
                                                   string_amount=form.cleaned_data['string_amount'],
                                                   price=form.cleaned_data['price'],)

            """ name = models.CharField(max_length=45, null=True)
            string_amount = models.IntegerField(null=True)
            price = models.IntegerField(null=True)
            neck_material = models.CharField(max_length=45, null=True)
            fretboard_material = models.CharField(max_length=45, null=True) # Field name made lowercase.
            pick_guard = models.NullBooleanField(null=True, default=False) # Field name made lowercase.
            type = models.CharField(max_length=45, null=True)
            body = EmbeddedModelField('Body', null=True)
            bridge = EmbeddedModelField('Bridge', null=True)
            pickups = EmbeddedModelField('Pickup', null=True)
            producer = EmbeddedModelField('Producer', null=True) """

            guitar.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Form is not valid')
    else:
        form = GuitarAddForm()
    return render(request,'guitar_app/add.html', {'form': form})