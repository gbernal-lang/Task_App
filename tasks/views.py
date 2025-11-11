
from django.views.generic.edit import CreateView
from .models import Task
# reverse_lazy se usa para obtener la URL al terminar correctamente la vista
from django.urls import reverse_lazy
#Se importa para que se puede mostrar los mensajes.
from django.contrib import messages
#Se importa para usar la la CBV de Delete
from django.views.generic import DeleteView
#Se importa para usar la la CBV de Update
from django.views.generic import UpdateView

from django.views.generic import ListView

#Clase para usar la clase Createview
class TaskCreate(CreateView):

    model = Task  #Nombre del modelo
    template_name = "tasks/task_view.html" #nombre del template en html
    success_url = reverse_lazy('task-list')  # Url a la cual se rederigira cuando se complete la tarea

# Campos del modelo que se mostrarán en el formulario
    fields = ['title', 'description','status']

#Función para  el mensaje de exito cuando se agrega una tarea
    def form_valid(self, form):
        messages.success(self.request, "La tarea se guardó exitosamente :)")
        return super().form_valid(form)

#Clase para usar la vista de Delete
class TaskDelete(DeleteView):
    model = Task
    template_name = "tasks/taskconfirm_delete.html" #Nombre del template usado para esta vista
    success_url = reverse_lazy('task-list') #Url a la cual se rederigira cuando se elimine una tarea

#Funcion para mostrar un mensaje cuando la tarea se haya eliminado
    def post(self, request, *args, **kwargs):
        messages.success(request, "La tarea se eliminó correctamente")
        return super().post(request, *args, **kwargs)


#Clase para usar la vista de Update
class TaskUpdate(UpdateView):
    model = Task
    template_name = "tasks/task_form.html" # Nombre del template usado para esta vista
    fields = ['title', 'description', 'status'] # Campos que se pueden editar
    success_url = reverse_lazy('task-list') # Url a la cual se rederigira cuando se edite y se guarde la tarea

    #Función para mostrar un mensaje de exito cuando se edite la tarea.
    def form_valid(self, form):
        messages.success(self.request, "La tarea se edito correctamente")
        return super().form_valid(form)

#Clase para Listview
class TaskListView(ListView):
    model = Task 
    template_name = "tasks/task_list.html" 
    context_object_name = "tasks"    
    



