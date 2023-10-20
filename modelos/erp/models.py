from django.db import models
from datetime import datetime

class Type(models.Model):...
    
# Create your models here.
class Alumnos(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=150, verbose_name='Nombres y Apellidos')
    dpi = models.CharField(max_length=13, unique= 10, verbose_name='DPI')
    date = models.DateField(verbose_name='Fecha de nacimiento')
    telefono = models.CharField(max_length=8, verbose_name='Telefono')
    user = models.CharField(max_length=10, verbose_name='Nombre de usuario')
    correo = models.CharField(max_length=30, verbose_name='Correo electronico')
    contraseña = models.CharField(max_length=25, verbose_name='Contraseña')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'alumno'
        verbose_name_plural = 'alumnos'
        db_table = 'alumno'
        ordering = ['id']
class Catedratico(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=150, verbose_name='Nombres y Apellidos')
    dpi = models.CharField(max_length=13, unique= 10, verbose_name='DPI')
    correo = models.CharField(max_length=30, verbose_name='Correo electronico')
    contraseña = models.CharField(max_length=25, verbose_name='Contraseña')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'catedratico'
        verbose_name_plural = 'catedraticos'
        db_table = 'catedratico'
        ordering = ['id']