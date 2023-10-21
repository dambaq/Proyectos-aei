from django.urls  import path
from Alumnos.views import alumnos_list



app_name = 'Alumnos'

urlpatterns = [
    path('alumnos/list/', alumnos_list, name='alumnos_list'),


]

