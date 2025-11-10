from django.views.generic.edit import CreateView
from .models import Task
# reverse_lazy se usa para obtener la URL al terminar correctamente la vista
from django.urls import reverse_lazy
#Se importa para que se puede mostrar los mensajes.
from django.contrib import messages
class TaskCreate(CreateView):

    # specify the model for create view
    model = Task
    template_name = "task_view.html" #nombre del template en html
    success_url = reverse_lazy('task-create')  # nombre de la url

    # specify the fields to be displayed
    fields = ['title', 'description','status']

#Función para  el mensaje de exito
    def form_valid(self, form):
        messages.success(self.request, "La tarea se guardó exitosamente :)")
        return super().form_valid(form)