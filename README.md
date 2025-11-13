# Buenas Prácticas de Programación

##  Variables de entorno (.env)

Se creó un archivo `.env` (no versionado) en la raíz del proyecto con los siguientes valores:

```bash
SECRET_KEY=gus12345
DEBUG=True

DB_NAME=task_app
DB_USER=dev_user
DB_PASSWORD=Dev2025
DB_HOST=localhost
DB_PORT=5432

## Después, se carga en settings.py

from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG") == "True"


### El archivo .env fue agregado al .gitignore para evitar exponer datos sensibles.

## Configuración de Logging en settings.py

LOGGING = {
    # Versión del esquema de configuración (siempre se deja en 1)
    "version": 1,

    # Permite mantener los loggers existentes del sistema (no los desactiva)
    "disable_existing_loggers": False,

    # -----------------------------------------------------------------
    # FORMATTERS: definen el formato con que se muestran los mensajes
    # -----------------------------------------------------------------
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
    },

    # -----------------------------------------------------------------
    # HANDLERS: definen **dónde** se van a enviar los logs
    # (a un archivo, a la consola, a un servicio, etc.)
    # -----------------------------------------------------------------
    "handlers": {
        "file": {
            "level": "INFO",  # Registra INFO, WARNING y ERROR
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "debug.log"),
            "formatter": "verbose",
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },

    # -----------------------------------------------------------------
    # LOGGERS: agrupan los mensajes por módulo o aplicación
    # -----------------------------------------------------------------
    "loggers": {
        "django": {
            "handlers": ["file", "console"],
            "level": "INFO",
            "propagate": True,
        },
        "tasks": {
            "handlers": ["file", "console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

### Se genera el archivo debug.log, donde se registran eventos del sistema y de la aplicación.

## Implementación de Logging en tasks/views.py

import logging
logger = logging.getLogger(__name__)

class TaskCreate(CreateView):
    model = Task
    template_name = "tasks/task_view.html"
    success_url = reverse_lazy("task-list")
    fields = ["title", "description", "status"]

    def form_valid(self, form):
        logger.info(f"Tarea creada: {form.instance.title}")  # Evento exitoso
        messages.success(self.request, "La tarea se guardó exitosamente :)")
        return super().form_valid(form)


## Configuración de Flake8

Se creó el archivo .flake8 en la raíz del proyecto con la siguiente configuración:

Configuración de estilo de código Python (PEP8)

[flake8]
max-line-length = 88
exclude = .git,__pycache__,venv,migrations

### Para ejecutar el control de calidad:

flake8 .


### Este comando revisa el cumplimiento de las normas PEP8 y detecta errores como:

Importaciones innecesarias

Comentarios incorrectos

Líneas demasiado largas

Código no utilizado


# Uso de Black

Black es un formateador automático de código Python.
Permite mantener un estilo uniforme en todo el proyecto.

### Para aplicarlo:

black .

### Este :

Reestructura el código automáticamente siguiendo el estándar PEP8.

Asegura que todo el equipo mantenga el mismo formato de escritura.

## Ejemplo del archivo debug.log

Cuando se crea una tarea, el log genera registros como los siguientes:

INFO 2025-11-13 10:48:34,517 views Tarea creada: Pruebas
INFO 2025-11-13 10:48:34,589 basehttp "POST /tasks/create/ HTTP/1.1" 302 0
INFO 2025-11-13 10:48:34,642 basehttp "GET /tasks/ HTTP/1.1" 200 3324


Estos registros permiten auditar la ejecución del sistema y verificar el flujo de las vistas.