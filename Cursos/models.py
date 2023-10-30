from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone



class Type(models.Model):...
    
# Create your models here.
class Cursos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=15)
    descripcion = models.CharField(max_length= 100)
    imagen = models.ImageField(upload_to='cursos', null=True, blank=True)
    disponibilidad= models.BooleanField(default= True)
    costo = models.FloatField(default=0.0)
    horario = models.CharField(max_length=20, default="Sin horario")
    created = models.DateField(default=timezone.now)
    updated = models.DateField(default=timezone.now)


    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

    def __str__(self):
        return self.name
    
class Asignacion(models.Model):
    alumno= models.ForeignKey(User, on_delete=models.CASCADE)
    cursos= models.ForeignKey(Cursos, on_delete=models.CASCADE)
    nota= models.FloatField(default=0.0)
    created = models.DateField(default=timezone.now)
    updated = models.DateField(default=timezone.now)

    class Meta:
        unique_together = ('alumno', 'cursos')
        verbose_name= 'Asinacion'
        verbose_name= 'Asignaciones'

    def __str__(self):
        return f"{self.alumno.username} : {self.cursos.name}"