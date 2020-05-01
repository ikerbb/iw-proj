from django.contrib import admin
from .models import Empleado,Tarea,Cliente,Proyecto

# Con esto registramos los modelos para poder tratarlos desde la aplicación de administrador

admin.site.register(Empleado)
admin.site.register(Tarea)
admin.site.register(Cliente)
admin.site.register(Proyecto)
