from django.urls import path
from .views import TaskDelete
from . import views
# importing views from views..py
from .views import TaskCreate

from .views import TaskUpdate
from .views import TaskListView


urlpatterns = [
    #Se agrega un nombre para identificar la url
    path('create/', TaskCreate.as_view(), name='task-create' ),
    # Ruta para eliminar una tarea existente.
    # <int:pk> indica que la vista recibirá el ID (primary key) de la tarea a eliminar.
    # Esta ruta muestra una página de confirmación y al aceptar elimina el registro.
    path('delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('edit/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('', TaskListView.as_view(), name='task-list'),


]

