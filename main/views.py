from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'AI-html-1.0.0/index.html')

def lista(request):
    return render(request,'AI-html-1.0.0/lista.html')

def iniciar(request):
    return render(request,'AI-html-1.0.0/iniciar.html')
def contact(request):
    return render(request,'AI-html-1.0.0/contact.html')
def inscripcion(request):
    return render(request,'AI-html-1.0.0/inscripcion.html')
