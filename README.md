# Manejar errores con try/except y archivo de logs.

En esta actividad se siguio usando LOGGING, que se integro en settings.py

```bash
LOGGING = {
    # Versión del esquema de configuración (siempre se deja en 1)
    "version": 1,

    # Permite mantener los loggers existentes del sistema (no los desactiva)
    "disable_existing_loggers": False,

    # -----------------------------------------------------------------
    # FORMATTERS: definen el formato con que se muestran los mensajes
    # -----------------------------------------------------------------
    "formatters": {
        "verbose": {  # Nombre del formato personalizado
            # Estructura del mensaje del log
            "format": "{levelname} {asctime} {module} {message}",
            # 'style' indica cómo se interpretan las llaves del formato
            "style": "{",
        },
    },

    # -----------------------------------------------------------------
    # HANDLERS: definen **dónde** se van a enviar los logs
    # (a un archivo, a la consola, a un servicio, etc.)
    # -----------------------------------------------------------------
    "handlers": {
        # Handler que escribe los logs en un archivo llamado "debug.log"
        "file": {
            "level": "INFO",  # Registra INFO, WARNING y ERROR
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "debug.log"),  # ruta del archivo
            "formatter": "verbose",  # usa el formato definido arriba
        },
        # Handler que muestra los logs directamente en la terminal
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },

    # -----------------------------------------------------------------
    # LOGGERS: agrupan los mensajes por módulo o aplicación
    # -----------------------------------------------------------------
    "loggers": {
        # Logger principal de Django (para mensajes del framework)
        "django": {
            "handlers": ["file", "console"],  # Muestra en archivo y consola
            "level": "INFO",  # Nivel mínimo a registrar
            "propagate": True,  # Permite que los mensajes se propaguen
        },

        # Logger específico de la app "tasks"
        "tasks": {
            "handlers": ["file", "console"],  # Mismos manejadores
            "level": "INFO",  # Solo muestra INFO o superior
            "propagate": False,  # Evita duplicar mensajes
        },
    },
}
```
## Asi mismo en Views.py, se agrego lo try/Exceptions, donde tambien se integraron los mensajes que se le mostraran al usuario.

```bash
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

```
### Todos estas mensajes se visualizan en el archivo debug.log y en las alertas que se implementaron en las vistas