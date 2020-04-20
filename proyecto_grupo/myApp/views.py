from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Proyecto, Empleado, Tarea, Cliente
from .forms import empleadoForm, proyectoForm, tareaForm, clienteForm


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

class CreateEmpleadosView(View):
    def get(self, request, *args, **kwargs):
        form = empleadoForm()
        context = {
            'form':form
        }
        return render(request, 'empleadoForm.html', context)

    def post(self, request, *args, **kwargs):
        form = empleadoForm(request.POST)
        if form.is_valid():
            empleado = Empleado()
            empleado.dni = form.cleaned_data['dni']
            empleado.nombre = form.cleaned_data['nombre']
            empleado.apellidos = form.cleaned_data['apellidos']
            empleado.email = form.cleaned_data['email']
            empleado.telefono = form.cleaned_data['telefono']
            empleado.estado = form.cleaned_data['estado']
            empleado.save()

            form.save()

            return redirect('empleados')

        return render('empleadoForm', {'form':form})

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



class CreateProyectoView(View):
    def get(self, request, *args, **kwargs):
        form = proyectoForm()
        context = {

        }
        return render(request, 'gestionar_proyecto.html', context)

    def post(self, request, *args, **kwargs):
        form = proyectoForm(request.POST)
        if form.is_valid():
            proyecto = Proyecto
            proyecto.nombre = form.cleaned_data['nombre']
            proyecto.descripcion = form.cleaned_data['descripcion']
            proyecto.fecha_inicio = form.cleaned_data['fecha_inicio']
            proyecto.fecha_fin = form.cleaned_data['fecha_fin']
            proyecto.presupuesto = form.cleaned_data['presupuesto']
            proyecto.cliente = form.cleaned_data['cliente']
            proyecto.empleados = form.cleaned_data['empleados']
            proyecto.save()

            form.save()

            return redirect('proyecto')

        return render('gestionar_proyecto', {'form':form})



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



class CreateTareasView(View):
    def get(self, request, *args, **kwargs):
        form = tareaForm()
        context = {
            'form':form
        }
        return render(request, 'anadir_tarea.html', context)

    def post(self, request, *args, **kwargs):
        form = tareaForm(request.POST)
        if form.is_valid():
            tarea = Tarea()
            tarea.nombre = form.cleaned_data['nombre']
            tarea.descripcion = form.cleaned_data['descripcion']
            tarea.fecha_inicio = form.cleaned_data['fecha_inicio']
            tarea.fecha_fin = form.cleaned_data['fecha_fin']
            tarea.responsable = form.cleaned_data['responsable']
            tarea.prioridad = form.cleaned_data['prioridad']
            tarea.estado = form.cleaned_data['estado']
            tarea.notas = form.cleaned_data['notas']

            tarea.save()

            form.save()

            return redirect('tareas')

        return render('añadir_tarea', {'form':form})


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



class CreateClientesView(View):
    def get(self, request, *args, **kwargs):
        form = clienteForm()
        context = {
            'form':form
        }
        return render(request, '.html', context)

    def post(self, request, *args, **kwargs):
        form = clienteForm(request.POST)
        if form.is_valid():
            cliente = Cliente()
            cliente.nombre = form.cleaned_data['nombre']
            cliente.empresa = form.cleaned_data['empresa']
            cliente.telefono = form.cleaned_data['telefono']
            cliente.email = form.cleaned_data['email']
            cliente.datos_adicionales = form.cleaned_data['datos_adicionales']

            cliente.save()

            form.save()

            return redirect('clientes')

        return render('', {'form':form})

