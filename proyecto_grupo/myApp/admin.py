from django.contrib import admin
from .models import Empleado,Tarea,Cliente,Proyecto

# Register your models here.

admin.site.register(Empleado)
admin.site.register(Tarea)
admin.site.register(Cliente)
admin.site.register(Proyecto)
