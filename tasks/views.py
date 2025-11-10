
from django.views.generic.edit import CreateView
from .models import Task
# reverse_lazy se usa para obtener la URL al terminar correctamente la vista
from django.urls import reverse_lazy
#Se importa para que se puede mostrar los mensajes.
from django.contrib import messages

from django.views.generic import DeleteView

from django.http import HttpResponse

class TaskCreate(CreateView):

    model = Task  #Nombre del modelo
    template_name = "task_view.html" #nombre del template en html
    success_url = reverse_lazy('task-create')  # nombre de la url

# Campos del modelo que se mostrarán en el formulario
    fields = ['title', 'description','status']

#Función para  el mensaje de exito
    def form_valid(self, form):
        messages.success(self.request, "La tarea se guardó exitosamente :)")
        return super().form_valid(form)


class TaskDelete(DeleteView):
    model = Task
    template_name = "taskconfirm_delete.html" #Template para deleteview
    success_url = reverse_lazy('tasks_index') #url que a la cual se redirije cuando se confirma la eliminación

#Funcion que muestra el mensaje de confirmacion.
    def form_valid(self, form):
        messages.success(self.request, "La tarea se eliminó correctamente :)")
        return super().form_valid(form)
    
#Vista basada en funciones, para verificar que funciona correctamente la vista de "delate"
def index(request):
    return HttpResponse("Gestor de tareas funcionando ✅")
