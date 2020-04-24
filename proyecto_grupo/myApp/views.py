from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic import DetailView, ListView
from .models import Proyecto, Empleado, Tarea, Cliente


def showInicio(request):
    return render(request, "index.html")


class EmpleadosListView(ListView):
    model = Empleado
    template_name = "empleadosListView.html"
    queryset = Empleado.objects.order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super(EmpleadosListView, self).get_context_data(**kwargs)
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


class EmpleadosDetailView(DetailView):
    model = Empleado
    template_name = "empleadosDetailView.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadosDetailView, self).get_context_data(**kwargs)
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


def showCreateEmpleadosView(request):
    return render(request, 'gestionar_empleado.html')


def postCreateEmpleadosView(request):
    dni = request.POST["dni"]
    nombre = request.POST["nombre"]
    apellidos = request.POST["apellidos"]
    email = request.POST["email"]
    telefono = request.POST["telefono"]
    estado = request.POST["estado"]

    empleado = Empleado()

    empleado.dni = dni
    empleado.nombre = nombre
    empleado.apellidos = apellidos
    empleado.email = email
    empleado.telefono = telefono
    empleado.estado = estado

    empleado.save()

    return redirect('empleadosListView')


class ProyectosListView(ListView):
    model = Proyecto
    template_name = "proyectosListView.html"
    queryset = Proyecto.objects.order_by('nombre')

    # cuando hagamos filtros cambiaremos esto para traer solo X proyectos, o ordenados por lo que sea

    def get_context_data(self, **kwargs):
        context = super(ProyectosListView, self).get_context_data(**kwargs)
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


class ProyectosDetailView(DetailView):
    model = Proyecto
    template_name = "proyectosDetailView.html"

    def get_context_data(self, **kwargs):
        context = super(ProyectosDetailView, self).get_context_data(**kwargs)
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


def showCreateProyectosView(request):
    return render(request, 'gestionar_proyecto.html')


def postCreateProyectosView(request):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    fecha_inicio = request.POST["fecha_inicio"]
    fecha_fin = request.POST["fecha_final"]
    presupuesto = request.POST["Presupuesto"]
    cliente = request.POST["cliente"]
    tareas = request.POST["tareas"]
    empleados = request.POST["empleados"]

    proyecto = Proyecto()

    proyecto.nombre = nombre
    proyecto.descripcion = descripcion
    proyecto.fecha_inicio = fecha_inicio
    proyecto.fecha_fin = fecha_fin
    proyecto.presupuesto = presupuesto
    proyecto.cliente = cliente
    proyecto.tareas = tareas
    proyecto.empleados = empleados

    proyecto.save()

    return redirect('proyectosListView')

class TareasListView(ListView):
    model = Tarea
    template_name = "tareasListView.html"
    queryset = Tarea.objects.order_by('nombre')

    def get_context_object_name(self, **kwargs):
        context = super(TareasListView, self).get_context_object_name(**kwargs)
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


class TareasDetailView(DetailView):
    model = Tarea
    template_name = "tareasDetailView.html"

    def get_context_data(self, **kwargs):
        context = super(TareasDetailView, self).get_context_data(**kwargs)
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


def showCreateTareasView(request):
    return render(request, 'gestionar_tarea.html')


def postCreateTareasView(request):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    fecha_inicio = request.POST["fecha_inicio"]
    fecha_fin = request.POST["fecha_fin"]
    responsable = request.POST["responsable"]
    prioridad = request.POST["prioridad"]
    estado = request.POST["estado"]
    notas = request.POST["notas"]

    tarea = Tarea()

    tarea.nombre = nombre
    tarea.descripcion = descripcion
    tarea.fecha_inicio = fecha_inicio
    tarea.fecha_fin = fecha_fin
    tarea.responsable = responsable
    tarea.prioridad = prioridad
    tarea.estado = estado
    tarea.notas = notas

    tarea.save()

    return redirect('tareasListView')


class ClientesListView(ListView):
    model = Cliente
    template_name = "clientesListView.html"
    queryset = Cliente.objects.order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super(ClientesListView, self).get_context_data(**kwargs)
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


class ClientesDetailView(DetailView):
    model = Cliente
    template_name = "clientesDetailView.html"

    def get_context_data(self, **kwargs):
        context = super(ClientesDetailView, self).get_context_data(**kwargs)
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


def showCreateClientesView(request):
    return render(request, 'gestionar_cliente.html')


def postCreateClientesView(request):
    nombre = request.POST["nombre"]
    empresa = request.POST["empresa"]
    telefono = request.POST["telefono"]
    email = request.POST["email"]
    datos_adicionales = request.POST["datos_adicionales"]

    cliente = Cliente()

    cliente.nombre = nombre
    cliente.empresa = empresa
    cliente.telefono = telefono
    cliente.email = email
    cliente.datos_adicionales = datos_adicionales


    cliente.save()

    return redirect('clientesListView')