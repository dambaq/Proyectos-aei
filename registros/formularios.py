from django import forms
from Alumnos.models import Alumnos

class Formalumno(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ('name','apellidos','dpi','date','telefono','correo')