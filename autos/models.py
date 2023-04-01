from django.db import models

# Create your models here.
class Autos(models.Model):
    nombre=models.CharField(max_length=50)
    marca=models.CharField(max_length=30)
    modelo=models.IntegerField()
    color=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    
  
    
class Clientes(models.Model):
    nombre=models.CharField(max_length=80)
    apellido=models.CharField(max_length=30)
    direccion=models.CharField(max_length=100)
    email=models.EmailField(max_length=70)
    telefono=models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
    

# from autos.models import *
# Autos.objects.create(nombre="connor",marca="mazda",modelo=2022,color="blanco")
# Autos.objects.create(nombre="toyota",marca="mazda",modelo="2023",color="negro") 
# Autos.objects.create(nombre="jaguar",marca="mek",modelo="2022",color="azul")  
# Autos.objects.create(nombre="honda",marca="branzai",modelo="2023",color="rojo")
# Autos.objects.create(nombre="zuzuki",marca="mazda",modelo="2020",color="morado")
# Clientes.objects.create(nombre="nilcen",apellido="mosquera",direccion="laguna",email="nilce@gmail.com",telefono="3117550785")
# Clientes.objects.create(nombre="sofia",apellido="pechene",direccion="colombiana",email="sofia@gmail.com",telefono="3154789541")
# Clientes.objects.create(nombre="israel",apellido="pechene",direcion="alpes",email="israelmosuqera@gmail.com",telefono="3124567889")
# Clientes.objects.create(nombre="israel",apellido="guerrero",direccion="alpes",email="israelpechene@gmail.com",telefono="3125678943")
# Clientes.objects.create(nombre="neider",apellido="taquinas",direccion="cruces",email="neider@gmail.com",telefono="3124567893")
# Clientes.objects.create(nombre="ronal",apellido="suares",direccion="corinto",email="ronales@gmail.com",telefono="3145678904")
