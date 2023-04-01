from django.shortcuts import render
from .models import *

# Create your views here.
def principal(request):
    datos={
        'titulo':'principal'
    }
    return render(request,'principal.html',datos)

def autos(request):
    datos={
        'titulo':'Autos',
        'autos':Autos.objects.all(),
    }
    return render(request,'autos.html',datos)

def clientes(request):
    datos={
        'titulo':'Clientes',
        'clientes':Clientes.objects.all(),

    }
    return render(request,'clientes.html',datos)



