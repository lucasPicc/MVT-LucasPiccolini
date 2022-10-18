from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar

# Create your views here.

def agregar_familiar(request,edad,nombre,nacimiento):

    familiar = Familiar(edad=edad, nombre=nombre, nacimiento=nacimiento)
    familiar.save()

    return HttpResponse(f'''
    <p>Familiar agregado<p>
    ''')

def mostrar_datos(request):
    datos = Familiar.objects.all()
    return render(request, 'plantilla1.html', {"datos_familiar": datos})

