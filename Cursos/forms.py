from django import forms
from Alumnos.models import Alumnos

class AsignacionForm(forms.Form):
    alumno = forms.ModelChoiceField(queryset=Alumnos.objects.all(), label="Seleccione un alumno")
