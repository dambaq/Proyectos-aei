from django.shortcuts import render, redirect
from .models import Cursos, Asignacion  # Importa el modelo Cursos desde el módulo actual
from Alumnos.models import Alumnos
from .forms import AsignacionForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

def cursos_lista(request):
    cursos = Cursos.objects.filter(disponibilidad= True)

    return render(request, 'list/lista.html', {'cursos': cursos})

def cursos_list(request):
    usuario = request.user
    asignaciones = Asignacion.objects.filter(alumno=usuario)
    asignados = [asignacion.cursos for asignacion in asignaciones]
    
    noasignados = Cursos.objects.filter(disponibilidad=True).exclude(id__in=[curso.id for curso in asignados])

    return render(request, 'list/list.html', {'noasignados': noasignados})

def cursos_noasignados(request):
    usuario = request.user
    asignaciones = Asignacion.objects.filter(alumno=usuario)
    asignados = [asignacion.cursos for asignacion in asignaciones]

    return render(request, 'list/listdes.html', {'asignados': asignados})

def asignar_alumno(request, curso_id, user_id):
    curso = Cursos.objects.get(pk=curso_id)
    alumno = User.objects.get(pk=user_id)

    asignacionexiste = Asignacion.objects.filter(alumno=alumno, cursos=curso).exists()

    if not asignacionexiste:
        asignacion = Asignacion(alumno=alumno, cursos=curso)
        asignacion.save()

    usuario = request.user
    asignaciones = Asignacion.objects.filter(alumno=usuario)
    asignados = [asignacion.cursos for asignacion in asignaciones]
    
    noasignados = Cursos.objects.filter(disponibilidad=True).exclude(id__in=[curso.id for curso in asignados])

    return render(request, 'list/list.html', {'noasignados': noasignados})

def desasignar_alumno(request, curso_id, user_id):
    curso = Cursos.objects.get(pk=curso_id)
    alumno = User.objects.get(pk=user_id)

    asignacionexiste = Asignacion.objects.filter(alumno=alumno, cursos=curso).exists()

    if asignacionexiste:
        desasignar = Asignacion.objects.filter(alumno=alumno, cursos=curso)
        desasignar.delete()

    usuario = request.user
    asignaciones = Asignacion.objects.filter(alumno=usuario)
    asignados = [asignacion.cursos for asignacion in asignaciones]

    return render(request, 'list/listdes.html', {'asignados': asignados})

def vistacursos(request, curso_id):
    curso=Cursos.objects.get(id=curso_id)
    
    return render(request, 'list/cursosindividuales.html', {'curso':curso})

@login_required
def enviarcursos(request):
    usuario = request.user

    asignaciones = Asignacion.objects.filter(alumno=usuario)

    cursos_info = "\n".join([f"{asignacion.cursos.name}" for asignacion in asignaciones])
    mensaje = f"Tus cursos asignados son:\n{cursos_info}"

    try:
        usuario_alumno = Alumnos.objects.get(user=usuario)
        correo_destino = usuario_alumno.correo
    except Alumnos.DoesNotExist:
        usuario_alumno = Alumnos.objects.get(user=usuario)
        correo_destino = usuario_alumno.correo 

    send_mail('Tus cursos asignados', mensaje, 'damaciob.98@gmail.com', [correo_destino])

    return redirect('perfil')
