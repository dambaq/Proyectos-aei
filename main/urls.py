from django.urls import path
from . import  views

urlpatterns = [
    path('home/', views.home, name= 'home'),
    path('lista/', views.lista, name= 'lista'),
    path('iniciar/', views.iniciar, name= 'iniciar'),
    path('contact/', views.contact, name= 'contact'),
    path('inscripcion/', views.inscripcion, name= 'inscripcion'),
    
]