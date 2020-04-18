from django.db import models

CHOICE_estado_empleado = [(0, 'Fijo'), (1, 'Eventual')]
CHOICE_prioridad = [(0, 'Alta'), (1, 'Media'), (2, 'Baja')]
CHOICE_estado_tarea = [(0, 'Sin empezar'), (1, 'En marcha'), (2, 'Acabada')]


class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    estado = models.IntegerField(choices=CHOICE_estado_empleado)


class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsable = models.ManyToManyField(Empleado)
    prioridad = models.IntegerField(choices=CHOICE_prioridad)
    estado = models.IntegerField(choices=CHOICE_estado_tarea)
    notas = models.CharField(max_length=10000, blank=True)


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=100)
    datos_adicionales = models.CharField(max_length=1000, blank=True)


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tareas = models.ManyToManyField(Tarea)
    empleados = models.ManyToManyField(Empleado)
