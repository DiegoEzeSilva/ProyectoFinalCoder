from django.db import models

class Empleado(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    celular = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class ProductosNuevos(models.Model):
    
    marca = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    largo = models.IntegerField()
    
    def __str__(self):
        return f'{self.marca} {self.version}'
    
    
class ProductosUsados(models.Model):
    
    marca = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    largo = models.IntegerField()
    
class Equipamiento(models.Model):
    
    Nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)