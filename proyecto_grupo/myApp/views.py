from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, DeleteView, UpdateView
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
        return context

class EmpleadosDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleadosDeleteView.html'
    success_url = reverse_lazy('empleadosListView')


class EmpleadosUpdateView(UpdateView):
    model = Empleado
    fields = '__all__'
    template_name = 'empleadosUpdateView.html'
    success_url = reverse_lazy('empleadosListView')


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

class ProyectosDeleteView(DeleteView):
    model = Proyecto
    template_name = 'proyectosDeleteView.html'
    success_url = reverse_lazy('proyectosListView')


class ProyectosUpdateView(UpdateView):
    model = Proyecto
    fields = '__all__'
    template_name = 'proyectosUpdateView.html'
    success_url = reverse_lazy('proyectosListView')


def showCreateProyectosView(request):
    empleado_list = Empleado.objects.order_by('nombre')
    clientes_list = Cliente.objects.order_by('nombre')
    context = {'empleado_list': empleado_list, 'clientes_list': clientes_list}
    return render(request, 'gestionar_proyecto.html', context)


def postCreateProyectosView(request):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    fecha_inicio = request.POST["fecha_inicio"]
    fecha_fin = request.POST["fecha_final"]
    presupuesto = request.POST["Presupuesto"]
    cliente = request.POST["cliente"]
    empleados = request.POST["empleados"]
    array_empleado = [empleados]

    proyecto = Proyecto()

    proyecto.nombre = nombre
    proyecto.descripcion = descripcion
    proyecto.fecha_inicio = fecha_inicio
    proyecto.fecha_fin = fecha_fin
    proyecto.presupuesto = presupuesto

    clientes = Cliente.objects.get(pk=cliente)
    proyecto.cliente = clientes

    empleado = Empleado.objects.get(pk=empleados)
    proyecto.empleados.add(empleado)

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

class TareasDeleteView(DeleteView):
    model = Tarea
    template_name = 'tareasDeleteView.html'
    success_url = reverse_lazy('tareasListView')


class TareasUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'tareasUpdateView.html'
    success_url = reverse_lazy('tareasListView')


def showCreateTareasView(request):
    return render(request, 'gestionar_tarea.html')


def postCreateTareasView(request):
    nombre_tarea = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    fecha_inicio = request.POST["fecha_inicio"]
    fecha_fin = request.POST["fecha_fin"]
    nombre = request.POST["responsable"]
    prioridad = request.POST["prioridad"]
    estado = request.POST["estado"]
    notas = request.POST["notas"]

    tarea = Tarea()

    tarea.nombre_tarea = nombre_tarea
    tarea.descripcion = descripcion
    tarea.fecha_inicio = fecha_inicio
    tarea.fecha_fin = fecha_fin
    tarea.nombre = nombre
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
        return context


class ClientesDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientesDeleteView.html'
    success_url = reverse_lazy('clientesListView')


class ClientesUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'clientesUpdateView.html'
    success_url = reverse_lazy('clientesListView')


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
