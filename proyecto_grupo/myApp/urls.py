from django.forms import forms
from django.urls import path
from . import views

#nombre de las urls creadas, junto con la vista que ejecuta cada una de ellas y el nombre que se usa para llamar a cada url desde los html creados.

urlpatterns = [
    path('', views.showInicio, name='index'),
    path('faq/', views.showFAQ, name='faq'),
    path('empleados/', views.EmpleadosListView.as_view(), name='empleadosListView'),
    path('empleados/<int:pk>/', views.EmpleadosDetailView.as_view(), name='empleadosDetailView'),
    path('empleados/registro/', views.showCreateEmpleadosView, name='registrarEmpleado'),
    path('empleados/registro/action',views.postCreateEmpleadosView, name='registroEmpleado'),
    path('empleados/actualizar/<int:pk>',views.EmpleadosUpdateView.as_view(), name='empleadosUpdateView'),
    path('empleados/borrar/<int:pk>', views.EmpleadosDeleteView.as_view(), name='empleadosDeleteView'),
    path('proyectos/', views.ProyectosListView.as_view(), name='proyectosListView'),
    path('proyectos/<int:pk>/', views.ProyectosDetailView.as_view(), name='proyectosDetailView'),
    path('proyectos/registro/', views.showCreateProyectosView, name='registrarProyecto'),
    path('proyectos/registro/action', views.postCreateProyectosView, name='registroProyecto'),
    path('proyectos/actualizar/<int:pk>/', views.ProyectosUpdateView.as_view(), name='proyectosUpdateView'),
    path('proyectos/borrar/<int:pk>/', views.ProyectosDeleteView.as_view(), name='proyectosDeleteView'),
    path('tareas/', views.TareasListView.as_view(), name='tareasListView'),
    path('tareas/<int:pk>/', views.TareasDetailView.as_view(), name='tareasDetailView'),
    path('tareas/registro/', views.showCreateTareasView, name='registrarTarea'),
    path('tareas/registro/action', views.postCreateTareasView, name='registroTarea'),
    path('tareas/actualizar/<int:pk>', views.TareasUpdateView.as_view(), name='tareasUpdateView'),
    path('tareas/borrar/<int:pk>/', views.TareasDeleteView.as_view(), name='tareasDeleteView'),
    path('clientes/', views.ClientesListView.as_view(), name='clientesListView'),
    path('clientes/<int:pk>/', views.ClientesDetailView.as_view(), name='clientesDetailView'),
    path('clientes/registro/', views.showCreateClientesView, name='registrarCliente'),
    path('clientes/registro/action', views.postCreateClientesView, name='registroCliente'),
    path('clientes/actualizar/<int:pk>/', views.ClientesUpdateView.as_view(), name='clientesUpdateView'),
    path('clientes/borrar/<int:pk>/', views.ClientesDeleteView.as_view(), name='clientesDeleteView')
]
