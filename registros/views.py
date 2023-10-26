from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .formularios import Formalumno
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from Cursos.models import Cursos, Asignacion

from django.shortcuts import get_object_or_404

# Create your views here.
class crearuser(View):
    def get(self, request):
        form=CustomUserCreationForm()
        formextra=Formalumno()
        return render(request,'inscripcion/inscripcion.html', {'form':form,'formextra':formextra})
    
    def post(self,request):
        form=CustomUserCreationForm(request.POST)
        formextra=Formalumno(request.POST)
        if form.is_valid() and formextra.is_valid():
            user=form.save()
            useralumno= formextra.save(commit=False)
  #          userimagen= request.Files['imagen']
            useralumno.user= user
            useralumno.save()
            login(request, user)
            return redirect('perfil')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request,'inscripcion/inscripcion.html', {'form':form,'formextra':formextra})
        
class CustomUserCreationForm(UserCreationForm):
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        # Personaliza tus propias restricciones aquí
        if len(password) < 8:
            raise forms.ValidationError(_("La contraseña debe tener al menos 8 caracteres."))
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError(_("La contraseña debe contener al menos un número."))
        if not any(char.isupper() for char in password):
            raise forms.ValidationError(_("La contraseña debe contener al menos una letra mayúscula."))
        if not any(char in "!@#$%^&*()" for char in password):
            raise forms.ValidationError(_("La contraseña debe contener al menos un símbolo: !@#$%^&*()"))
        return password
        
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def iniciar_sesion(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            usuario=authenticate(username=username,password=password)

            if usuario is not None:
                login(request, usuario)
                return redirect('perfil')
            else:
                messages.error(request,'Usuario y/o contraseña incorrecta')
        else:
            messages.error(request, 'Usuario y/o contraseña incorrecta')

    form=AuthenticationForm()
    return render(request,'login/login.html',{'form':form})    

@login_required
def perfil(request):
    usuario = request.user
    asignaciones = Asignacion.objects.filter(alumno=usuario)
    asignados = [asignacion.cursos for asignacion in asignaciones]# Lógica para obtener los datos del estudiante y cursos asignados
        # ...
    return render(request, 'perfil/perfil.html', {'asignados': asignados})
 
def informacion(request):
    usuario = request.user
    asignaciones = Asignacion.objects.filter(alumno=usuario)
    asignados = [asignacion.cursos for asignacion in asignaciones]# Lógica para obtener los datos del estudiante y cursos asignados
        # ...
    return render(request, 'perfil/informacion.html', {'asignados': asignados})
