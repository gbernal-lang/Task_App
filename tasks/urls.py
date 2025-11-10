from django.urls import path

from .views import TaskDelete
from . import views


urlpatterns = [
    # Ruta para eliminar una tarea existente.
    # <int:pk> indica que la vista recibirá el ID (primary key) de la tarea a eliminar.
    # Esta ruta muestra una página de confirmación y al aceptar elimina el registro.
    path('delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('', views.index, name='tasks_index'),

]