from django.db import models

#Clase para los clientes, donde se establecen las características a rellenar de todos los clientes que se incluyan.


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=100)
    datos_adicionales = models.CharField(max_length=1000, blank=True)

    # Con esta función determinamos qué datos mostrar del objeto en sitios como la app de administración

    def __str__(self):
        return f'{self.id}, {self.nombre}, {self.empresa}'

#Clase para los empleados, donde se establecen las características a rellenar de los empleados que se incluyan.


class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    estado = models.CharField(max_length=100)

    # Con esta función determinamos qué datos mostrar del objeto en sitios como la app de administración

    def __str__(self):
        return f'{self.id}, {self.nombre}, {self.apellidos}'

#Clase para los proyectos, donde se establecen las características a rellenar de los proyectos que se incluyan.

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleados = models.ManyToManyField(Empleado, blank=True, null=True)

    #Con esta función determinamos qué datos mostrar del objeto en sitios como la app de administración

    def __str__(self):
        return f'{self.id}, {self.nombre}'

#Clase para las tareas, donde se establecen las características a rellenar de las tareas que se incluyan.


class Tarea(models.Model):
    nombre_tarea = models.CharField(max_length=100)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=1000)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    nombre = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    prioridad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    notas = models.CharField(max_length=10000, blank=True)

    # Con esta función determinamos qué datos mostrar del objeto en sitios como la app de administración

    def __str__(self):
        return f'{self.id}, {self.nombre_tarea}'






