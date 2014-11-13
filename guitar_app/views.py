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

def get_max_guitar_id():
    max_id = None
    if models.Guitars.objects.all():
        max_id = models.Guitars.objects.order_by('-id')[0].id #order by desc, get first elem id
    if not max_id:
        max_id = 0
    return max_id

def get_max_body_id():
    max_id = None
    if models.Body.objects.all():
        max_id = models.Body.objects.order_by('-id')[0].id #order by desc, get first elem id
    if not max_id:
        max_id = 0
    return max_id

def get_max_producer_id():
    max_id = None
    if models.Producer.objects.all():
        max_id = models.Producer.objects.order_by('-id')[0].id #order by desc, get first elem id
    if not max_id:
        max_id = 0
    return max_id

def add(request):
    if request.method == 'POST':
        form = GuitarAddForm(request.POST)
        if form.is_valid():
            max_guitar_id = get_max_guitar_id()
            max_body_id = get_max_body_id()
            max_producer_id = get_max_producer_id()
            models.Guitars(
               id=int(max_guitar_id)+1,
               name=form.cleaned_data['name'],
               string_amount=form.cleaned_data['string_amount'],
               price=form.cleaned_data['price'],
               neck_material=form.cleaned_data['neck_material'],
               fretboard_material=form.cleaned_data['fretboard_material'],
               pick_guard=form.cleaned_data['pick_guard'],
               type=form.cleaned_data['type'],
               body=models.Body(id = int(max_body_id) + 1,
                          material=form.cleaned_data['body_material'],
                          color=form.cleaned_data['body_color'],
                          type=form.cleaned_data['body_type'],
                          form=form.cleaned_data['body_form']).save(),
               producer=models.Producer(id=int(max_producer_id)+1,
                          name=form.cleaned_data['producer_name'],
                          rating=form.cleaned_data['producer_rating'],
                          info=form.cleaned_data['producer_info']).save()).save()

            #guitar.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Form is not valid')
    else:
        form = GuitarAddForm()
    return render(request,'guitar_app/add.html', {'form': form})