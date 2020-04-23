from django.forms import forms
from django.urls import path
from . import views

urlpatterns = [
    path('empleados/', views.EmpleadosListView.as_view(), name='empleadosListView'),
    path('empleados/<int:pk>/', views.EmpleadosDetailView.as_view(), name='empleadosDetailView'),
    path('empleados/registro/', views.showCreateEmpleadosView, name='registrarEmpleado'),
    path('empleados/registro/action',views.postCreateEmpleadosView, name='registroEmpleado'),
    path('proyectos/', views.ProyectosListView.as_view(), name='proyectosListView'),
    path('proyectos/<int:pk>/', views.ProyectosDetailView.as_view(), name='proyectosDetailView'),
    path('proyectos/registro/', views.showCreateProyectosView, name='registrarProyecto'),
    path('proyectos/registro/action', views.postCreateProyectosView, name='registroProyecto'),
    path('tareas/', views.TareasListView.as_view(), name='tareasListView'),
    path('tareas/<int:pk>/', views.TareasDetailView.as_view(), name='tareasDetailView'),
    path('tareas/registro/', views.showCreateTareasView, name='registrarTarea'),
    path('tareas/registro/action', views.postCreateTareasView, name='registroTarea'),
    path('clientes/', views.ClientesListView.as_view(), name='clientesListView'),
    path('clientes/<int:pk>/', views.ClientesDetailView.as_view(), name='clientesDetailView'),
    path('clientes/registro/', views.showCreateClientesView, name='registrarCliente'),
    path('clientes/registro/action', views.postCreateClientesView, name='registroCliente'),
    path('',views.showInicio, name='index')
]
