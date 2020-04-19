from .models import Empleado, Tarea, Proyecto, Cliente, CHOICE_prioridad
from django import forms

class empleadoForm(forms.Form):
        class Meta:
                model = Empleado
                fields = '__all__'


class tareaForm(forms.Form):
        class Meta:
                model = Tarea
                fields = '__all__'
