from django.db import models

# Create your models here.
class Autos (models.model):
    nombre=models.CharField(max_length=50)
    marca=models.CharField(max_length=30)
    modelo=models.IntegerField()
    color=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre
    
  
    
class Clientes(models.Model):
    nombre=models.CharField(max_length=80)
    apellido=models.CharField(max_length=30)
    direccion=models.CharField(max_length=100)
    email=models.EmailField(max_length=70)
    telefono=models.CharField(max_length=10)