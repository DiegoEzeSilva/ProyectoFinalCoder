from django.http import HttpResponse
from django.shortcuts import render
from .models import Empleado, ProductosNuevos, ProductosUsados, Equipamiento
from .forms import EmpleadoFormulario, ProductosNuevosFormulario, ProductosUsadosFormulario, EquipamientosFormulario

# Create your views here.

def empleado(req, nombre, apellido, email, celular):
    
    empleado = Empleado(nombre=nombre, apellido=apellido, email=email, celular=celular)
    empleado.save()
    
    return HttpResponse(f"""
                        <p>Empleado: {empleado.nombre} {empleado.apellido} agregado!</p>
    """)

def productos_nuevos(req, marca, version, largo):
    
    productos_nuevos = ProductosNuevos(marca=marca, version=version, largo=largo)
    productos_nuevos.save()
    
def productos_usados(req, marca, version, largo):
    
    productos_usados = ProductosUsados(marca=marca, version=version, largo=largo)
    productos_usados.save()
    
def equipamiento(req, Nombre, descripcion):
    
    equipamiento = Equipamiento(Nombre=Nombre, descripcion=descripcion)
    equipamiento.save()