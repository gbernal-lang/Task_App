###########################################################
## Módulo: views.py (Vistas de la aplicación de tareas)
## Descripción: Contiene las vistas basadas en clases (CBV) para crear, 
##              listar, actualizar y eliminar tareas. Implementa mensajes 
##              de confirmación y redirección tras cada acción.
## Fecha de creación: 2025/Noviembre/06
## Autor: GH (Gustavo Hernández)
## Fecha de última modificación: 2025/Noviembre/12
## Autor última modificación: GH
## Comentarios de última modificación: Se agregaron comentarios
## descriptivos
###########################################################

#Se importa para usar la vista generica de Createview
from django.views.generic.edit import CreateView
from .models import Task
# reverse_lazy se usa para obtener la URL al terminar correctamente la vista
from django.urls import reverse_lazy
#Se importa para que se puede mostrar los mensajes.
from django.contrib import messages
#Se importa para usar la vista generica de Deleteview
from django.views.generic import DeleteView
#Se importa para usar la vista generica de Updateview
from django.views.generic import UpdateView
#Se importa para usar la vista generica de Listview
from django.views.generic import ListView

from .forms import TaskCreateForm

# Clase para crear nuevas tareas
class TaskCreate(CreateView):

    model = Task  # Nombre del modelo
    template_name = "tasks/task_view.html" #Nombre del template en html
    form_class = TaskCreateForm #Modelform utilizado
    success_url = reverse_lazy('task-list')  # URL de redirección tras guardar una tarea

# Muestra un mensaje de éxito cuando se agrega una tarea
    def form_valid(self, form):
        messages.success(self.request, "La tarea se guardó exitosamente :)")
        return super().form_valid(form)
    #Muestra un mensaje cuando hay error en los campos del formulario
    def form_invalid(self, form):

        messages.error(self.request, "Revisa los campos del formulario")
        return super().form_invalid(form)
    

# Clase para eliminar tareas existentes
class TaskDelete(DeleteView):
    model = Task
    template_name = "tasks/taskconfirm_delete.html" # Template utilizado para confirmar la eliminación
    success_url = reverse_lazy('task-list') # URL de redirección tras eliminar la tarea

 # Muestra un mensaje cuando la tarea se elimina correctamente
    def post(self, request, *args, **kwargs):
        messages.success(request, "La tarea se eliminó correctamente")
        return super().post(request, *args, **kwargs)


# Clase para actualizar tareas existentes
class TaskUpdate(UpdateView):
    model = Task
    template_name = "tasks/task_form.html" # Template utilizado para editar tareas
    form_class = TaskCreateForm #Modelform creado
    success_url = reverse_lazy('task-list') # URL de redirección tras guardar los cambios

    # Muestra un mensaje de éxito cuando se edita la tarea
    def form_valid(self, form):
        messages.success(self.request, "La tarea se edito correctamente")
        return super().form_valid(form)
    #Muestra un mensaje cuando los datos de los campos no son los correctos
    def form_invalid(self, form):

         messages.error(self.request, "Revisa los campos del formulario")
        
         return super().form_invalid(form)

# Clase para listar todas las tareas registradas
class TaskListView(ListView):
    model = Task 
    template_name = "tasks/task_list.html" # Template que muestra la lista de tareas
    context_object_name = "tasks"          # Nombre del contexto utilizado en el template
    



