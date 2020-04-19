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


class proyectoForm(forms.Form):
    class Meta:
        model = Proyecto
        exclude = ['tareas']


class clienteForm(forms.Form):
    class Meta:
        model = Cliente
        fields = '__all__'
