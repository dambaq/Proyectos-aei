from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import crearuser, cerrar_sesion, iniciar_sesion

urlpatterns = [
    path('',crearuser.as_view(), name='registro'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    path('iniciar_sesion', iniciar_sesion, name='iniciar_sesion'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)