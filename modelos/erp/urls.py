from django.urls  import path
from modelos.erp.views.alumnos.views import alumnos_list
from modelos.login.views import *


app_name = 'modelos.erp'

urlpatterns = [
    path('alumnos/list/', alumnos_list, name='alumnos_list'),
    path('login/', LoginFormView.as_view()),


]

