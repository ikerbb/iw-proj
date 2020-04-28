from django.db import models


#Clase para los empleados, donde se establecen las características a rellenar de los empleados que se incluyan.
#Cada dato tendrá un tamaño máximo a incluir, excepto el telefono del empleado.
#Al final mostrará por pantalla el id, nombre y apellidos del empleado.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=100)
    datos_adicionales = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.id}, {self.nombre}, {self.empresa}'

class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    estado = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}, {self.nombre}, {self.apellidos}'

#Clase para las tareas, donde se establecen las características a rellenar de las tareas que se incluyan.
#Todos los datos de las tareas tendrán un tamaño máximo, excluyendo las fechas de inicio y de fin.
#Al final mostrará por pantalla el id y el nombre de la tarea.
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

    def __str__(self):
        return f'{self.id}, {self.nombre_tarea}'

#Clase para los clientes, donde se establecen las características a rellenar de todos los clientes que se incluyan.
#Todos los datos de los clientes tendrán un tamaño máximo a incluir, excepto el teléfono.
#Al final, mostrará por pantalla el id, nombre y la empresa del cliente.



#Clase para los proyectos, donde se establecen las características a rellenar de todos los proyectos que se incluyan.
#Todos los datos de los clientes tendrán un tamaño máximo a incluir, excepto las fechas y el presupuesto.
#Al final, se mostrará por pantalla el id y el nombre de los proyectos.


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tareas = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    empleados = models.ManyToManyField(Empleado, blank=True)
