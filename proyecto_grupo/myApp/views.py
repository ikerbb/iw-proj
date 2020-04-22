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


def showCreateEmpleadosView(request):
    return render(request, 'gestionar_empleado.html')


def postCreateEmpleadosView(request):
    dni = request.POST["dni"]
    nombre = request.POST["nombre"]
    apellidos = request.POST["apellidos"]
    email = request.POST["email"]
    telefono = request.POST["telefono"]
    estado = request.POST["estado"]
    empleado = Empleado(dni, nombre, apellidos, email, telefono, estado)
    empleado.save()


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
            'form': form
        }
        return render(request, 'gestionar_proyecto.html', context)

    def post(self, request, *args, **kwargs):
        form = proyectoForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('proyecto')

        return render(request, 'gestionar_proyecto.html', {'form': form})


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
            'form': form
        }
        return render(request, 'gestionar_tarea.html', context)

    def post(self, request, *args, **kwargs):
        form = tareaForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('tareas')

        return render(request, 'añadir_tarea', {'form': form})


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
            'form': form
        }
        return render(request, 'gestionar_clientes.html', context)

    def post(self, request, *args, **kwargs):
        form = clienteForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('clientes')

        return render(request, 'gestionar_clientes.html', {'form': form})
