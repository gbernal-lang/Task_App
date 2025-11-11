from django.urls import path
from . import views
#De Views se importan las vistas creadas
from .views import TaskCreate
from .views import TaskDelete
from .views import TaskUpdate
from .views import TaskListView


urlpatterns = [
    #Se agrega un nombre para identificar la url
    path('create/', TaskCreate.as_view(), name='task-create' ),
    # Ruta para eliminar una tarea existente.
    # <int:pk> indica que la vista recibirá el ID (primary key) de la tarea a eliminar.
    # Esta ruta muestra una página de confirmación y al aceptar elimina el registro.
    path('delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    #Igual se le indica un ID, para identificar que tarea es la que se va a editar
    path('edit/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('', TaskListView.as_view(), name='task-list'),


]

