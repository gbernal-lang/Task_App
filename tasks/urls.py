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

from django.urls import path
from . import views

# Importación de las vistas definidas en views.py
from .views import TaskCreate, TaskDelete, TaskUpdate, TaskListView


urlpatterns = [
    # Ruta para crear una nueva tarea
    path("create/", TaskCreate.as_view(), name="task-create"),
    # Ruta para eliminar una tarea existente.
    # <int:pk> indica que la vista recibirá el ID (primary key) de la tarea a eliminar.
    # Muestra una página de confirmación y, al aceptar, elimina el registro.
    path("delete/<int:pk>/", TaskDelete.as_view(), name="task-delete"),
    # Ruta para editar una tarea existente mediante su ID
    path("edit/<int:pk>/", TaskUpdate.as_view(), name="task-update"),
    # Ruta principal que muestra la lista de tareas registradas
    path("", TaskListView.as_view(), name="task-list"),
]
