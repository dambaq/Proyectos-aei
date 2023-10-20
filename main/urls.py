from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name= 'home'),
    path('lista/', views.lista, name= 'lista'),
    path('iniciar/', views.iniciar, name= 'iniciar'),
    path('contact/', views.contact, name= 'contact'),
    path('inscripcion/', views.inscripcion, name= 'inscripcion'),
    path('erp/', include('modelos.erp.urls'))
    
]