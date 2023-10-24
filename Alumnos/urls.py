from django.urls  import path
from Alumnos.views import alumnos_list
from django.conf.urls.static import static
from django.conf import settings



app_name = 'Alumnos'

urlpatterns = [
    path('alumnos/list/', alumnos_list, name='alumnos_list'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)