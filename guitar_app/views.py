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
    if request.method == 'POST':
        form = GuitarAddForm(request.POST)
        if form.is_valid():
            guitar = models.Guitars.objects.get(pk=pk)
            t = GuitarAddForm(request.POST, instance=guitar)
            t.save()
            return HttpResponseRedirect('/')
    else:
        form = GuitarAddForm(instance=models.Guitars.objects.get(pk=pk))
        return render(request, 'guitar_app/guitar_detail.html', {'form': form, 'pk': pk})

def action(request):
    if request.method == 'POST':
        action = request.POST.get('action', False)
        if action:
            pks = request.POST.getlist("selection")
            #selected_objects = models.Guitar.objects.filter(pk__in=pks)
            if action == 'delete':
                models.Guitars.objects.filter(pk__in=pks).delete()
        return HttpResponseRedirect('/')
    return HttpResponse('no POST in action view')

def get_max_guitar_id():
    max_id = None
    if models.Guitars.objects.all():
        max_id = models.Guitars.objects.order_by('-id')[0].id #order by desc, get first elem id
    if not max_id:
        max_id = 0
    return max_id

def add(request):
    if request.method == 'POST':
        form = GuitarAddForm(request.POST)
        if form.is_valid():
            max_guitar_id = get_max_guitar_id()
            models.Guitars(
               id=int(max_guitar_id)+1,
               name=form.cleaned_data['name'],
               string_amount=form.cleaned_data['string_amount'],
               price=form.cleaned_data['price'],
               neck_material=form.cleaned_data['neck_material'],
               fretboard_material=form.cleaned_data['fretboard_material'],
               pick_guard=form.cleaned_data['pick_guard'],
               type=form.cleaned_data['type'],
               body_material=form.cleaned_data['body_material'],
               body_color=form.cleaned_data['body_color'],
               body_type=form.cleaned_data['body_type'],
               body_form=form.cleaned_data['body_form'],
               producer_name=form.cleaned_data['producer_name'],
               producer_rating=form.cleaned_data['producer_rating'],
               producer_info=form.cleaned_data['producer_info'],
               bridge_name=form.cleaned_data['bridge_name'],
               bridge_material=form.cleaned_data['bridge_material'],
               bridge_color=form.cleaned_data['bridge_color'],
               pickup_type=form.cleaned_data['pickup_type'],
               pickup_set_type=form.cleaned_data['pickup_set_type'],).save()
            #guitar = models.Guitars(pk=int(max_guitar_id)+1).save()
            #t = GuitarAddForm(request.POST, instance=guitar)
            #t.save()
            #guitar.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Form is not valid')
    else:
        form = GuitarAddForm()
    return render(request,'guitar_app/add.html', {'form': form})