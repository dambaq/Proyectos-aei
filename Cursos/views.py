from django.shortcuts import render
from .models import Cursos  # Importa el modelo Cursos desde el módulo actual

def cursos_list(request):
    cursos = Cursos.objects.all()  # Consulta la base de datos para obtener todos los cursos

    data = {
        'title': 'Listado de cursos',
        'cursos': cursos,  # Pasa la lista de cursos a la plantilla
    }

    return render(request, 'list/list.html', data)
