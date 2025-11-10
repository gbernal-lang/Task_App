from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib import messages
from .models import Task
from django.http import HttpResponse

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