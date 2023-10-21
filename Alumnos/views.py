from django.shortcuts import render 
from Alumnos.models import Alumnos

def home(request):
    # Lógica de la vista
    return render(request, 'index.html')

def alumnos_list(request):
    data = {
        'title' : 'Listado de alumnos',
        'alumnos' : Alumnos.objects.all()


    }
    return render(request, 'alumnos/list.html',data)

def inscripcion(request):
    # Lógica de la vista
    return render(request, 'inscripcion.html')