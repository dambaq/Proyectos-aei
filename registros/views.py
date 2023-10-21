from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .formularios import Formalumno
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages

# Create your views here.
class crearuser(View):
    def get(self, request):
        form=UserCreationForm()
        formextra=Formalumno()
        return render(request,'inscripcion/inscripcion.html', {'form':form,'formextra':formextra})
    
    def post(self,request):
        form=UserCreationForm(request.POST)
        formextra=Formalumno(request.POST)
        if form.is_valid() and formextra.is_valid():
            user=form.save()
            useralumno= formextra.save(commit=False)
  #          userimagen= request.Files['imagen']
            useralumno.user= user
            useralumno.save()
            login(request, user)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request,'inscripcion/inscripcion.html', {'form':form,'formextra':formextra})
        
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
                return redirect('home')
            else:
                messages.error(request,'ususario y/o contraseña incorrecta')
        else:
            messages.error(request, 'datos incorrectos')

    form=AuthenticationForm()
    return render(request,'login/login.html',{'form':form})    