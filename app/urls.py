from django.contrib import admin
from django.urls import path,include
from .views import*

urlpatterns=[
    path('Autos/',Autos,name='Autos'),
    path('Clientes/',Clientes,name='Clientes'),
    path('',Principal, name='Principal'),

]