from django.shortcuts import render 
from modelos.erp.models import Alumnos

def alumnos_list(request):
    data = {
        'title' : 'Listado de alumnos',
        'alumnos' : Alumnos.objects.all()


    }
    return render(request, 'alumnos/list.html',data)