from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('empleados/', views.EmpleadosListView.as_view(), name='empleadosListView'),
    path('empleados/<int:pk>/', views.EmpleadosDetailView.as_view(), name='empleadosDetailView'),
    path('proyectos/', views.ProyectosListView.as_view(), name='proyectosListView'),
    path('proyectos/<int:pk>/', views.ProyectosDetailView.as_view(), name='proyectosDetailView'),
    path('tareas/', views.TareasListView.as_view(), name='tareasListView'),
    path('tareas/<int:pk>/', views.TareasDetailView.as_view(), name='tareasDetailView'),
    path('clientes/', views.ClientesListView.as_view(), name='clientesListView'),
    path('clientes/<int:pk>/', views.ClientesDetailView.as_view(), name='clientesDetailView')
]
