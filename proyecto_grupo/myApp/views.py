from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, DeleteView, UpdateView
from .models import Proyecto, Empleado, Tarea, Cliente, Pregunta


# Funcion que muestra el menú de inicio

def showInicio(request):
    return render(request, "index.html")


# Funcion que muestra la pantalla con la página FAQ

def showFAQ(request):
    return render(request, "faq.html")

@method_decorator(csrf_exempt, name='dispatch')
class PreguntasView(View):
    def get(self, request):
        lista = Pregunta.objects.all()
        return JsonResponse(list(lista.values()), safe=False)

    def post(self, request):
        usuario = request.POST['usuario']
        titulo = request.POST['titulo']
        mensaje = request.POST['mensaje']

        pregunta = Pregunta()

        pregunta.usuario = usuario
        pregunta.titulo = titulo
        pregunta.mensaje = mensaje

        pregunta.save()

        return redirect('faq')

# Clase que se encarga de mostrar el listado de empleados

class EmpleadosListView(ListView):
    model = Empleado
    template_name = "empleadosListView.html"
    queryset = Empleado.objects.order_by('nombre')

    # Funcion que genera el contenido del diccionario que se le pasa a la pagina

    def get_context_data(self, **kwargs):
        context = super(EmpleadosListView, self).get_context_data(**kwargs)
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


# Clase que se encarga de mostrar los detalles de un empleado

class EmpleadosDetailView(DetailView):
    model = Empleado
    template_name = "empleadosDetailView.html"

    # Funcion que genera el contenido del diccionario que se le pasa a la pagina

    def get_context_data(self, **kwargs):
        context = super(EmpleadosDetailView, self).get_context_data(**kwargs)
        return context


# Clase que se encarga de realizar el borrado de un objeto Empleado

class EmpleadosDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleadosDeleteView.html'
    success_url = reverse_lazy('empleadosListView')


# Clase que se encarga de actualizar los datos de un objeto Empleado

class EmpleadosUpdateView(UpdateView):
    model = Empleado
    fields = '__all__'
    template_name = 'empleadosUpdateView.html'
    success_url = reverse_lazy('empleadosListView')


# Funcion que se encarga de mostrar el formulario para crear empleados

def showCreateEmpleadosView(request):
    return render(request, 'gestionar_empleado.html')


# Funcion que se encarga de recoger los datos introducidos en el formulario de creacion de empleados
# Una vez hecho el guardado en BBDD, redirige al usuario a la pagina con el listado de empleados

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
    txtdata = "/../static/email/email.txt"
    miEmail = "deustotiltech@gmail.com"
    destinatario = f"ikerbb@opendeusto.es, ainara11.lopez@opendeusto.es, aritz.saez@opendeusto.es, {email}"
    cuerpo = f"Buenos días: se ha registrado un nuevo empleado en la base de datos. Nombre: {nombre}; Apellidos: {apellidos}. Un saludo "
    mensaje = MIMEMultipart("plain")
    mensaje["From"] = miEmail
    mensaje["To"] = destinatario
    mensaje["Subject"] = "Confirmación de alta de empleado"
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    destinatario = f"ikerbb@opendeusto.es, ainara11.lopez@opendeusto.es, aritz.saez@opendeusto.es, {email}"
#    adjunto.set_payload(open("email.txt", "rb").read())
#    adjunto.add_header("content-Disposition", 'attachment; filename="email.txt"')
#    mensaje.attach(adjunto)
    smtp = SMTP("smtp.gmail.com")
    smtp.starttls()
    smtp.login(miEmail, "ikerainaraaritz")
    smtp.sendmail(miEmail, destinatario, mensaje.as_string())
    smtp.quit()

    return redirect('empleadosListView')




# Clase para la visualizacion del listado de Proyectos

class ProyectosListView(ListView):
    model = Proyecto
    template_name = "proyectosListView.html"
    queryset = Proyecto.objects.order_by('nombre')

    # Funcion que genera el contenido del diccionario que se le pasa a la pagina

    def get_context_data(self, **kwargs):
        context = super(ProyectosListView, self).get_context_data(**kwargs)
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context




# Clase que se encarga de mostrar en detalle un proyecto

def verProyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    empleados = proyecto.empleados.all()
    context = {'proyecto': proyecto, 'empleados': empleados}
    return render(request, 'proyectosDetailView.html', context)


# Clase que realiza el borrado de un objeto Proyecto

class ProyectosDeleteView(DeleteView):
    model = Proyecto
    template_name = 'proyectosDeleteView.html'
    success_url = reverse_lazy('proyectosListView')


# Clase que realiza la actualizacion de los datos de un objeto proyecto

class ProyectosUpdateView(UpdateView):
    model = Proyecto
    fields = '__all__'
    template_name = 'proyectosUpdateView.html'
    success_url = reverse_lazy('proyectosListView')


# Clase que muestra el formulario para la creación de objetos Proyecto

def showCreateProyectosView(request):
    empleado_list = Empleado.objects.order_by('nombre')
    clientes_list = Cliente.objects.order_by('nombre')
    context = {'empleado_list': empleado_list, 'clientes_list': clientes_list}
    return render(request, 'gestionar_proyecto.html', context)


# Clase que se encarga de recoger los datos introducidos en el formulario, crear el objeto y guardarlo en BBDD
# Al terminar, redirige al listado de Proyectos

def postCreateProyectosView(request):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    fecha_inicio = request.POST["fecha_inicio"]
    fecha_fin = request.POST["fecha_final"]
    presupuesto = request.POST["Presupuesto"]
    cliente = request.POST["cliente"]

    proyecto = Proyecto()

    proyecto.nombre = nombre
    proyecto.descripcion = descripcion
    proyecto.fecha_inicio = fecha_inicio
    proyecto.fecha_fin = fecha_fin
    proyecto.presupuesto = presupuesto

    proyecto.cliente = Cliente.objects.get(pk=cliente)
    proyecto.save()

    empleado_List = request.POST.getlist("empleados")

    for emp in empleado_List:
        empleado = Empleado.objects.get(pk=emp)
        proyecto.empleados.add(empleado)
    proyecto.save()

    return redirect('proyectosListView')


# Clase para la visualización del listado de Tareas

class TareasListView(ListView):
    model = Tarea
    template_name = "tareasListView.html"
    queryset = Tarea.objects.order_by('nombre')

    # Funcion que genera el contenido del diccionario que se le pasa a la pagina

    def get_context_data(self, **kwargs):
        context = super(TareasListView, self).get_context_data(**kwargs)
        return context

# Clase para la vista en detalle de una tarea

class TareasDetailView(DetailView):
    model = Tarea
    template_name = "tareasDetailView.html"

    # Funcion que genera el contenido del diccionario que se le pasa a la pagina

    def get_context_data(self, **kwargs):
        context = super(TareasDetailView, self).get_context_data(**kwargs)
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


# Clase encargada de realizar el borrado de una tarea

class TareasDeleteView(DeleteView):
    model = Tarea
    template_name = 'tareasDeleteView.html'
    success_url = reverse_lazy('tareasListView')


# Clase encargada de realizar la actualización de los datos de una tarea

class TareasUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'tareasUpdateView.html'
    success_url = reverse_lazy('tareasListView')


# Funcion que muestra el formulario de creación de una tarea

def showCreateTareasView(request):
    proyecto_list = Proyecto.objects.order_by('nombre')
    responsable_list = Empleado.objects.order_by('nombre')
    context = {'proyecto_list': proyecto_list, 'responsable_list': responsable_list}
    return render(request, 'gestionar_tarea.html', context)


# Clase que recoge los datos introducidos en el formulario, crea el objeto y lo guarda en BBDD

def postCreateTareasView(request):
    nombre_tarea = request.POST["nombre"]
    proyecto = request.POST["proyecto"]
    descripcion = request.POST["descripcion"]
    fecha_inicio = request.POST["fecha_inicio"]
    fecha_fin = request.POST["fecha_fin"]
    nombre = request.POST["responsable"]
    prioridad = request.POST["prioridad"]
    estado = request.POST["estado"]
    notas = request.POST["notas"]

    tarea = Tarea()

    tarea.nombre_tarea = nombre_tarea
    proyectos = Proyecto.objects.get(pk=proyecto)
    tarea.proyecto = proyectos
    tarea.descripcion = descripcion
    tarea.fecha_inicio = fecha_inicio
    tarea.fecha_fin = fecha_fin
    Nombre = Empleado.objects.get(pk=nombre)
    tarea.nombre = Nombre
    tarea.prioridad = prioridad
    tarea.estado = estado
    tarea.notas = notas

    tarea.save()

    return redirect('tareasListView')


# Clase para la visualizacion del listado de clientes

class ClientesListView(ListView):
    model = Cliente
    template_name = "clientesListView.html"
    queryset = Cliente.objects.order_by('nombre')

    # Funcion que genera el contenido del diccionario que se le pasa a la pagina

    def get_context_data(self, **kwargs):
        context = super(ClientesListView, self).get_context_data(**kwargs)
        # anadir context['dato'] = 'informacion' que es lo que irá a la plantilla
        return context


# Clase para la visualización en detalle de un cliente

class ClientesDetailView(DetailView):
    model = Cliente
    template_name = "clientesDetailView.html"

    # Funcion que genera el contenido del diccionario que se le pasa a la pagina

    def get_context_data(self, **kwargs):
        context = super(ClientesDetailView, self).get_context_data(**kwargs)
        return context


# Clase para el borrado de un objeto cliente

class ClientesDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientesDeleteView.html'
    success_url = reverse_lazy('clientesListView')


# Clase para la actualizacion de los datos de un objeto cliente

class ClientesUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'clientesUpdateView.html'
    success_url = reverse_lazy('clientesListView')


# Funcion que muestra el formulario para la creacion de un objeto cliente

def showCreateClientesView(request):
    return render(request, 'gestionar_cliente.html')


# Funcion que recoge los datos del formulario, crea el objeto y lo guarda en BBDD
# Redirige al listado de clientes

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
