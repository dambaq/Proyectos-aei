from django.urls  import path
from django.conf.urls.static import static
from django.conf import settings
from Cursos.views import cursos_list



app_name = 'Cursos'

urlpatterns = [
    path('cursos/list/', cursos_list, name='list_list'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)