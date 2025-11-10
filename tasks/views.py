from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import Task
from django.http import HttpResponse
from django.contrib import messages

class TaskUpdate(UpdateView):
    model = Task
    template_name = "task_form.html" # Template del formulario
    fields = ['title', 'description', 'status'] #Campos que se pueden editar
    success_url = reverse_lazy('tasks_index')
    
#Vista basada en funciones, para verificar que se ve en el servidor local
def index(request):
    return HttpResponse("Pagina de prueba ✅")

#Función para mostrar un mensaje de exito.
def form_valid(self, form):
        messages.success(self.request, "La tarea se edito correctamente :)")
        return super().form_valid(form)