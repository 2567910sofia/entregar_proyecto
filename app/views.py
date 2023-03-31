from django.shortcuts import render
from .models import *

# Create your views here.
def Principal(request):
    datos={
        'titulo':'principal'

    }
    return render(request,'principal.html',datos)

def Autos(request):
    datos={
        'titulo':'Autos',
        'Autos':Autos.object.all(),
    }
    return render(request,'Autos.html',datos)

def clientes(request):
    datos={
        'titulo':'Clientes',
        'Clientes':Clientes.objects.all(),

    }
    return render(request,'Clientes.html',datos)



