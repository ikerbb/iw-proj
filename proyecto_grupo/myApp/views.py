from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Proyecto, Empleado, Tarea, Cliente
<<<<<<< HEAD

=======
>>>>>>> master

def index(request):
    return HttpResponse("Texto de prueba")

<<<<<<< HEAD

=======
>>>>>>> master
class EmpleadosListView(ListView):
    model = Empleado
    template_name = "empleadosListView.html"
    queryset = Empleado.objects.order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super(EmpleadosListView, self).get_context_data(**kwargs)
<<<<<<< HEAD
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


=======
        #anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context

>>>>>>> master
class EmpleadosDetailView(DetailView):
    model = Empleado
    template_name = "empleadosDetailView.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadosDetailView, self).get_context_data(**kwargs)
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context

<<<<<<< HEAD

=======
>>>>>>> master
class ProyectosListView(ListView):
    model = Proyecto
    template_name = "proyectosListView.html"
    queryset = Proyecto.objects.order_by('nombre')
<<<<<<< HEAD

    # cuando hagamos filtros cambiaremos esto para traer solo X proyectos, o ordenados por lo que sea

    def get_context_data(self, **kwargs):
        context = super(ProyectosListView, self).get_context_data(**kwargs)
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


=======
    #cuando hagamos filtros cambiaremos esto para traer solo X proyectos, o ordenados por lo que sea

    def get_context_data(self, **kwargs):
        context = super(ProyectosListView, self).get_context_data(**kwargs)
        #anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context

>>>>>>> master
class ProyectosDetailView(DetailView):
    model = Proyecto
    template_name = "proyectosDetailView.html"

    def get_context_data(self, **kwargs):
        context = super(ProyectosDetailView, self).get_context_data(**kwargs)
<<<<<<< HEAD
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


=======
        #anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context

>>>>>>> master
class TareasListView(ListView):
    model = Tarea
    template_name = "tareasListView.html"
    queryset = Tarea.objects.order_by('nombre')

    def get_context_object_name(self, **kwargs):
        context = super(TareasListView, self).get_context_object_name(**kwargs)
<<<<<<< HEAD
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


=======
        #anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context

>>>>>>> master
class TareasDetailView(DetailView):
    model = Tarea
    template_name = "tareasDetailView.html"

    def get_context_data(self, **kwargs):
        context = super(TareasDetailView, self).get_context_data(**kwargs)
<<<<<<< HEAD
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


=======
        #anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context

>>>>>>> master
class ClientesListView(ListView):
    model = Cliente
    template_name = "clientesListView.html"
    queryset = Cliente.objects.order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super(ClientesListView, self).get_context_data(**kwargs)
<<<<<<< HEAD
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


=======
        #anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context

>>>>>>> master
class ClientesDetailView(DetailView):
    model = Cliente
    template_name = "clientesDetailView.html"

    def get_context_data(self, **kwargs):
        context = super(ClientesDetailView, self).get_context_data(**kwargs)
<<<<<<< HEAD
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


=======
        #anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context
>>>>>>> master
