from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


class Type(models.Model):...
    
# Create your models here.
class Alumnos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=15)
    apellidos = models.CharField(max_length=20)
    dpi = models.CharField()
    date = models.DateField()
    telefono = models.CharField()
    correo = models.CharField()
#    imagen = models.ImageField(upload_to='alumnos', null=True, blank=True)
    created = models.DateField(default=timezone.now)
    updated = models.DateField(default=timezone.now)


    class Meta:
        verbose_name = 'alumno'
        verbose_name_plural = 'alumnos'

    def __str__(self):
        return self.names