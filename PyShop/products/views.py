from django.shortcuts import render
from django.http import HttpResponse
from .models import MiProducto, MiOferta


# Create your views here.

def index(req):
    # también hay objects.filter/save/get...
    productos = MiProducto.objects.all()
    return render(req, 'index.html', 
                  {'products':productos})

def new(req):
    return HttpResponse("ahora estpas en new :)")