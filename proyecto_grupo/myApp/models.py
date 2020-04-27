from django.db import models



class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    estado = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}, {self.nombre}, {self.apellidos}'



class Tarea(models.Model):
    nombre_tarea = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    nombre = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    prioridad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    notas = models.CharField(max_length=10000, blank=True)

    def __str__(self):
        return f'{self.id}, {self.nombre_tarea}'


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=100)
    datos_adicionales = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.id}, {self.nombre}, {self.empresa}'


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tareas = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    empleados = models.ManyToManyField(Empleado, blank=True)

    def __str__(self):
        return f'{self.id}, {self.nombre}'


