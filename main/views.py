from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'AI-html-1.0.0/index.html')

def lista(request):
    return render(request,'AI-html-1.0.0/lista.html')