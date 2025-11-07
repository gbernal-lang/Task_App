#Archivo de urls de la apliacion.
#En este archivo se colocan las urls de las vistas que se quieran visualizar

from django.urls import path


#Se importa la vista desde el archivo views.py
from .views import TaskListView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
]
