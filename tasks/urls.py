###########################################################
## Módulo: urls.py (Rutas de la aplicación de tareas)
## Descripción: Define las rutas (URLs) para crear, editar, eliminar 
##              y listar tareas, conectando cada una con su vista 
##              correspondiente.
## Fecha de creación: 2025/Noviembre/06
## Autor: GH (Gustavo Hernández)
## Fecha de última modificación: 2025/Noviembre/12
## Autor última modificación: GH
## Comentarios de última modificación: Se agregaron comentarios explicativos 
##              
###########################################################

# tasks/urls.py

from django.urls import path
from . import views # Importamos el módulo completo 'views'

urlpatterns = [
    # Ruta para crear una nueva tarea
    path('create/', views.TaskCreate.as_view(), name='task-create'),

    # Ruta para eliminar una tarea existente.
    path('delete/<int:pk>/', views.TaskDelete.as_view(), name='task-delete'),

    # Ruta para editar una tarea existente mediante su ID
    path('edit/<int:pk>/', views.TaskUpdate.as_view(), name='task-update'),

    # Ruta principal que muestra la lista de tareas registradas
    path('', views.TaskListView.as_view(), name='task-list'),

    # Ruta para forzar un error
    path('glitchtip-debug/', views.trigger_error, name='glitchtip-debug'), 
    
   
]

