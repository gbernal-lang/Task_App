#Archivo de vistas
#Se crea una vista para el modelo que se creo, especificando cual es el que se quiere mostras

#Se importa el modelo del archivo models.py
from .models import Task

from django.views.generic import ListView
class TaskListView(ListView):
    model = Task #nombre del modelo
    template_name = "task_list.html" #nombre del template en html
    context_object_name = "tasks"
