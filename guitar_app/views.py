from django.shortcuts import render
from guitar_app import tables, models
from django_tables2   import RequestConfig
from django.http import HttpResponse, HttpResponseRedirect
from forms import *

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
            guitar = form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Form is not valid')
    else:
        form = GuitarAddForm()
    return render(request,'guitar_app/add.html', {'form': form})