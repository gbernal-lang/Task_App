# Se importa el módulo logging para registrar eventos, errores y mensajes informativos
import logging

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

# Se crea una instancia del logger para este módulo (views.py)
# Permite identificar de dónde proviene cada mensaje en el archivo de logs
logger = logging.getLogger(__name__)

# Clase para crear nuevas tareas
class TaskCreate(CreateView):

    model = Task  # Nombre del modelo
    template_name = "tasks/task_view.html" #Nombre del template en html
    success_url = reverse_lazy('task-list')  # URL de redirección tras guardar una tarea

# Campos del modelo que se mostrarán en el formulario
    fields = ['title', 'description','status']

# Muestra un mensaje de éxito cuando se agrega una tarea
    def form_valid(self, form):
        try:
           logger.info(f"Tarea creada: {form.instance.titlle}") # Registra un evento exitoso
           messages.success(self.request, "La tarea se guardó exitosamente :)")
           return super().form_valid(form)
        except Exception as e:
         logger.error(f"Error al crear tarea: {e}")
        # Muestra un mensaje de error al usuario en la interfaz
        messages.error(self.request, "Ocurrió un error al crear la tarea.")
        # Retorna form_invalid para que el formulario no se procese
        return self.form_invalid(form)
    




# Clase para eliminar tareas existentes
class TaskDelete(DeleteView):
    model = Task
    template_name = "tasks/taskconfirm_delete.html" # Template utilizado para confirmar la eliminación
    success_url = reverse_lazy('task-list') # URL de redirección tras eliminar la tarea

 # Muestra un mensaje cuando la tarea se elimina correctamente
    def post(self, request, *args, **kwargs):
        # Se usa para registrar un evento importante
        # o inusual, pero no es un error. 
        task = self.get_object()
        logger.warning(f"Tarea eliminada: {task.title}") 
        messages.success(request, "La tarea se eliminó correctamente")
        return super().post(request, *args, **kwargs)


# Clase para actualizar tareas existentes
class TaskUpdate(UpdateView):
    model = Task
    template_name = "tasks/task_form.html" # Template utilizado para editar tareas
    fields = ['title', 'description', 'status'] # Campos que se pueden editar
    success_url = reverse_lazy('task-list') # URL de redirección tras guardar los cambios

    # Muestra un mensaje de éxito cuando se edita la tarea
    def form_valid(self, form):
        try:
               logger.info(f"Tarea Editada correctamente: {form.instance.titllle}") # Registra un evento exitoso
               
               messages.success(self.request, "La tarea se edito correctamente")
               return super().form_valid(form)
        
        except Exception as e:
               logger.error(f"Error al editar la tarea: {e}")
               messages.error(self.request, "Ocurrior un error al editar la tarea")
               return self.form_invalid(form)



# Clase para listar todas las tareas registradas
class TaskListView(ListView):
    model = Task 
    template_name = "tasks/task_list.html" # Template que muestra la lista de tareas
    context_object_name = "tasks"          # Nombre del contexto utilizado en el template
    



