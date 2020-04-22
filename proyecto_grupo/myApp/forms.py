from .models import Empleado, Tarea, Proyecto, Cliente, CHOICE_prioridad
from django import forms


class empleadoForm(forms.ModelForm):
    
    class Meta:
        model = Empleado
        fields = '__all__'


class tareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = '__all__'


class proyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        exclude = ['tareas']


class clienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
