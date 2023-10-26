from django.urls  import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.cursos_list, name='list_list'),
    path('lista/', views.cursos_lista, name='list_lista'),
    path('curso_asignados/', views.cursos_noasignados, name='list_listdes'),
    path('asignar_alumno/<int:curso_id>/<int:user_id>/', views.asignar_alumno, name='asignar_alumno'),
    path('desasignar_alumno/<int:curso_id>/<int:user_id>/', views.desasignar_alumno, name='desasignar_alumno'),
    path('vistacursos/<int:curso_id>/', views.vistacursos, name= 'vista_cursos'),
    path('correo/', views.enviarcursos, name='enviar')


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
