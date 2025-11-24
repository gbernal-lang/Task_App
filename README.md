# Informe Técnico

Esta fase tuvo como propósito aprender y aplicar conceptos fundamentales de JavaScript, manejo de logs, buenas prácticas de programación y la integración de herramientas de monitoreo para mejorar la observabilidad de aplicaciones.

En este caso primero se crearon las variables de entorno.

## Archivo ,env
El archivo .env se utiliza para mover parámetros configurables como nivel de log, rutas o entradas sensibles, permitiendo cambiar el comportamiento del logging sin modificar el código.

```bash
SECRET_KEY=gus12345
DEBUG=True

DB_NAME=task_app
DB_USER=dev_user
DB_PASSWORD=Dev2025
DB_HOST=localhost
DB_PORT=5432
```

## Configuración de Logging en settings.py

Esta configuración define cómo, dónde y con qué formato Django registrará los mensajes del sistema (logs).
El propósito es tener visibilidad del comportamiento de la aplicación, detectar errores, advertencias y eventos importantes durante el desarrollo o producción.

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

```

Esto crea un archivo debug.log, donde se mostraran todos los mensajes o advertencias que se hayan,
implementado.

## Debug.log

```bash
INFO 2025-11-13 10:48:34,517 views Tarea creada: Pruebas
INFO 2025-11-13 10:48:34,589 basehttp "POST /tasks/create/ HTTP/1.1" 302 0
INFO 2025-11-13 10:48:34,642 basehttp "GET /tasks/ HTTP/1.1" 200 3324
```

# Try / Except

Los bloques try / except se utilizan para manejar errores sin que el programa se detenga.
En lugar de que la aplicación falle cuando ocurre un error, puedes interceptarlo, controlarlo y decidir qué hacer.

Son esenciales para:

evitar que la aplicación se caiga,

mostrar mensajes más claros,

registrar errores en logs,

continuar la ejecución aun cuando algo falla.

En este caso se siguio utilizando la configuración de loggin y se implementaron
en una vista.

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

Todos estas mensajes se visualizan en el archivo debug.log y en las alertas que se implementaron en las vistas.

# Validaciones y formularios con Django Forms y ModelForms

Django Forms y ModelForms permiten validar que los datos ingresados por los usuarios sean correctos antes de guardarlos. Las validaciones personalizadas (clean_<campo>) se usan para aplicar reglas específicas, como longitudes mínimas o campos obligatorios. Además, el método form_invalid permite mostrar mensajes de error amigables al usuario cuando el formulario contiene datos incorrectos.

Para esto en el formulario, se integraron validaciónes personalizadas.

```bash
 #Validación personalizada para titulo
    def clean_title(self):
        title = self.cleaned_data.get('title') #Obtiene lo que se haya ingresado en este campo
        #Si no se ingresa un titulo manda este error
        if  not title:
         
             raise forms.ValidationError("El Titulo es obligatorio")
        #Si el titulo tiene menos de 3 caracteres, manda el siguiente mensaje
        if len (title)<3:
         
            raise forms.ValidationError("El nombre del titulo debe de  tener mas de 3 caracteres")

        return title 
    #Validación personalizada para descripción
    def clean_description(self):
        description = self.cleaned_data.get('description')
        #Si el campo descripción esta vacio, muestra el siguiente mensaje
        if not description:
            raise forms.ValidationError("La descripción es obligatoria")
        #Si el campo tiene menos de 3 caracteres,muestra el siguiente mensaje
        if len (description)<3:
            raise forms.ValidationError("La descripción debe tener mas de 3 caracteres")
        return description



```

Después, en el archvio views.py, se coloca un mensajes para informar al usuario sobre el problema.

```bash
# Muestra un mensaje cuando hay error en los campos del formulario
    def form_invalid(self, form):

        messages.error(self.request, "Revisa los campos del formulario")
        return super().form_invalid(form)

```

#  Interactividad con JavaScript

Para mejorar la actividad se creo un archivo base html, esto para no duplicar codigo
en cada template.

```bash
<!DOCTYPE html>
<html lang="es">

<!-- Carga la etiqueta "static" para poder usar archivos estáticos como CSS o JS -->
{% load static %}

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'tasks/style2.css' %}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <title>{% block title %}Gestión de Tareas{% endblock %}</title>
</head>
<body>
    
<!-- Verifica si existen mensajes enviados desde las vistas (éxito o error) -->
<!-- Si los hay, los recorre y muestra una alerta emergente con SweetAlert -->
{% if messages %}
  {% for message in messages %}
  <script>
    Swal.fire({
      icon: "success",
      title: "{{ message|escapejs }}",
      showConfirmButton: false,
      timer: 2200
    });
  </script>
  {% endfor %}
{% endif %}

 <!-- Contenido de cada página -->
    <main>
        {% block content %}
        {% endblock %}
    </main>

    <!-- JS global -->
    <script src="{% static 'js/task.js' %}"></script>

    {% block extra_js %}{% endblock %}

</body>
</html>

```

Después, en la carpeta de static se creo el archivo js, en donde se encuentran todas las 
funciones para filtrar las tareas y validar si hay campos vacios o no, además, se implemento
la funcionalidad basada en fetch, para saber el numero de tareas sin las necesidad de,
recargar la pagina.

```bash

//Validación de Formularios
//Evita el envío si hay campos vacios y muestra una alerta

document.addEventListener("DOMContentLoaded", () => {
    //Obtiene el formulario presente (Si existe)
    const form = document.querySelector("form");
    // Si existe el formulario, se agrega un validador al evento "submit"
    if (form) {
        form.addEventListener("submit", function (e) {
            //Obtiene los campos del formulario por ID
            const title = document.querySelector("#id_title");
            const description = document.querySelector("#id_description");

            //Verifica si estan vacios o contienen espacios
            if (!title.value.trim() || !description.value.trim()) {
                e.preventDefault();// si esta vacios o con espacios, no se hace el envio

                //Se muestra la alerta
                Swal.fire({
                    icon: "warning",
                    title: "Campos incompletos",
                    text: "Completa los campos antes de enviar.",
                    confirmButtonText: "Aceptar"
                });
            }
        });
    }
});


// FILTRAr tareas
// Permite buscar tareas en tiempo real sin recargar

// Input donde el usuario escribe el texto para filtrar
const filtro = document.getElementById("filtro");
//Coleccion de filas de tabla que contienen tareas
const filas = document.querySelectorAll("#task-table-body tr");

// Evento que se activa cada vez que el usario presiona una tecla
filtro.addEventListener("keyup", () => {
    // Trasnforma el texto ingresado a minisculas para comparar correctamente
    const texto = filtro.value.toLowerCase();

// Recorre cada fila de la tabla
    filas.forEach(fila => {
        // Obtiene titulo y descripcion desde los atributos personalizados
        const title = fila.dataset.title.toLowerCase();
        const description = fila.dataset.description.toLowerCase();

        // Si el texto buscado coincide con alguno, se muestra la fila
        if (title.includes(texto) || description.includes(texto)) {
            fila.style.display = ""; // Muestra la fila
        } else {
            fila.style.display = "none"; // Oculta fila
        }
    });
});


/**
* Función encargada de obtener mediante una petición fetch
 * el número total de tareas registradas en el servidor
 * y actualizar dinámicamente el contenido del elemento HTML
 * con id="total-tasks" sin necesidad de recargar la página.
 */ 
function actualizarTotalTareas(){
    // Realiza una solicitud HTTP GET a la ruta definida
    fetch("/tasks/task-count/")
    // Convierte la respuesta obtenida a formato json
    .then(response => response.json())
    // Maneja el objeto de datos devuelto por el servidor
    .then(data => {
        // Inserta el valor recibido (data.total) dentro del elemento HTML con id "total-tasks"
        document.getElementById("total-tasks").textContent = data.total;
    } )
    // Si hay un error lo muestra en la consola
    .catch(error => console.error("Error en el fetch"));
}

// Evento que asegura que el código se ejecute únicamente
// cuando el DOM haya sido cargado completamente,
// evitando errores al intentar acceder a elementos inexistentes.
document.addEventListener("DOMContentLoaded", actualizarTotalTareas);

```
Después, se creó una nueva vista basada en funciones con el propósito de exponer la cantidad total de tareas registradas en la base de datos. Esta vista retorna los datos en formato JSON, lo que permite su consumo mediante fetch en el frontend.

```bash
def task_count(request):
    # Obtiene la cantidad total de registros almacenados en el modelo Task
    count = Task.objects.count()
    # Retorna la respuesta en formato JSON con la clave 'total'
    return JsonResponse ({"total":count})

```

Finalmente se agregar una url, apuntando a la función con petición fetch, asi mismo, en task_list.html se se agrega la barra de busqueda para filtrar tareas y una etiqueta para ver el numero de tareas sin recargar la pagina.

```bash
    #Endpoint que permite obtener el número total de tareas registradas
    # Este endpoint es consumido mediante la función fetch
    # y retorna un JSON con el conteo total de registros del modelo Task.

    path("task-count/", task_count, name="task-count")

```

# Pruebas automatizadas con pytest o unittest.

En esta parte se utilizo la herramienta de pytest, por lo cual se instalo y se creo un archvio test_view.py, 
este contendra acciones como las de insertar o eliminar una tarea.

```bash
from django.test import TestCase
from django.urls import reverse
from .models import Task

# Clase que agrupa las pruebas automatizadas para las vistas de Task
class TaskViewTests(TestCase):

    def test_task_list_view(self):
        """
        Caso 1: La vista de listado debe regresar 200.
        Validamos que la URL de lista funcione y cargue la plantilla correcta.
        """
        # Realiza una petición GET a la vista 'task-list'
        response = self.client.get(reverse('task-list'))

        # Verifica que la respuesta sea 200 OK
        self.assertEqual(response.status_code, 200)

        # Verifica que se haya renderizado el template correcto
        self.assertTemplateUsed(response, "tasks/task_list.html")

    def test_create_task(self):
        """
        Caso 2: Crear una tarea debe guardarla en la base de datos.
        Probamos que un POST cree correctamente una nueva tarea.
        """
        # Datos que se enviarán al formulario
        data = {
            "title": "Tarea de prueba",
            "description": "Probando creación",
            "status": "PENDIENTE"
        }

        # Enviar los datos mediante POST a la URL 'task-create'
        response = self.client.post(reverse('task-create'), data)

        # Después de crear, la vista debe redirigir (código 302)
        self.assertEqual(response.status_code, 302)

        # Validamos que ahora exista una tarea en la base
        self.assertEqual(Task.objects.count(), 1)

        # Verificamos que la tarea creada tenga el título correcto
        self.assertEqual(Task.objects.first().title, "Tarea de prueba")

    def test_delete_task(self):
        """
        Caso 3: Eliminar una tarea existente.
        Probamos que una tarea se elimine correctamente desde la vista.
        """
        # Crear una tarea temporal que luego será eliminada
        task = Task.objects.create(
            title="Eliminar",
            description="Tarea a eliminar",
            status="PENDIENTE"
        )

        # Enviar POST a la vista de eliminar tarea
        response = self.client.post(reverse('task-delete', args=[task.id]))

        # La vista debe redirigir después de eliminar (código 302)
        self.assertEqual(response.status_code, 302)

        # Validamos que ya no exista ninguna tarea en la BD
        self.assertEqual(Task.objects.count(), 0)


```
Después, en la raiz del proyecto se crea el archivo pytest.ini,
esto para configurar otras cuestiones de la herramienta.

```bash
[pytest]

# Indica a pytest qué settings de Django debe cargar
# para poder ejecutar las pruebas dentro del entorno
# adecuado del proyecto.
DJANGO_SETTINGS_MODULE = app.settings

# Define los patrones de nombres de archivos que pytest
# reconocerá como archivos de pruebas.
# - tests.py
# - test_*.py     (por ejemplo: test_views.py)
# - *_tests.py    (por ejemplo: views_tests.py)
python_files = tests.py test_*.py *_tests.py


```

# Herramienta open source para gestión colaborativa de errores.

Para esta parte, se utilizo la herramienta de GlitchTip, para monitorear los errores,
Por lo cual, se instalo de manera local, utilizando docker.

```bash
services:
  postgres:
    image: postgres:14-alpine
    restart: unless-stopped
    volumes:
      - postgres-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=glitchtip
      - POSTGRES_USER=glitchtip
      - POSTGRES_PASSWORD=glitchtip

  redis:
    image: redis:7-alpine
    restart: unless-stopped

  glitchtip:
    image: glitchtip/glitchtip:latest
    restart: unless-stopped
    command: sh -c "python manage.py migrate --noinput && gunicorn --bind 0.0.0.0:8000 glitchtip.wsgi"
    depends_on:
      - postgres
      - redis
    environment:
      - DJANGO_SETTINGS_MODULE=glitchtip.settings
      - DATABASE_URL=postgres://glitchtip:glitchtip@postgres:5432/glitchtip
      - REDIS_URL=redis://redis:6379/1
      - SECRET_KEY=1234567891011121314151617181920
      - DEBUG=True
      - EMAIL_URL=consolemail://  # Agrega esto para evitar errores de email
    ports:
      - "8000:8000"

  # WORKER DE CELERY - ESTO ES LO QUE FALTABA
  worker:
    image: glitchtip/glitchtip:latest
    restart: unless-stopped
    command: celery -A glitchtip worker -l INFO
    depends_on:
      - postgres
      - redis
      - glitchtip
    environment:
      - DJANGO_SETTINGS_MODULE=glitchtip.settings
      - DATABASE_URL=postgres://glitchtip:glitchtip@postgres:5432/glitchtip
      - REDIS_URL=redis://redis:6379/1
      - SECRET_KEY=1234567891011121314151617181920
      - EMAIL_URL=consolemail://

  # BEAT DE CELERY (opcional pero recomendado para tareas programadas)
  beat:
    image: glitchtip/glitchtip:latest
    restart: unless-stopped
    command: celery -A glitchtip beat -l INFO
    depends_on:
      - postgres
      - redis
    environment:
      - DJANGO_SETTINGS_MODULE=glitchtip.settings
      - DATABASE_URL=postgres://glitchtip:glitchtip@postgres:5432/glitchtip
      - REDIS_URL=redis://redis:6379/1
      - SECRET_KEY=1234567891011121314151617181920
      - EMAIL_URL=consolemail://

volumes:
  postgres-data:


```
Después, de esto se tuvo que instalar el sdk de sentry, esto para poder hacer la comunición de django hacia, el servidor de glitchtip.
Esto se configuro en el archivo de settings del proyecto.

```bash

# Inicializa el SDK de GlitchTip para capturar errores en Django
sentry_sdk.init(
    # DSN (Data Source Name): clave pública + URL del servidor + ID del proyecto.
    # Permite que la aplicación envíe errores al servidor de Sentry/GlitchTip.
    dsn="http://9eebc2a03fef4208a86411a561bdf87b@localhost:8000/1",

    # Integración específica para Django:
    # habilita la captura automática de excepciones, errores en vistas,
    # información del request, usuario autenticado, etc.
    integrations=[DjangoIntegration()],

    # Modo debug del SDK:
    # muestra en consola los eventos enviados, útil para pruebas locales.
    debug=True,

    # Entorno donde corre este proyecto:
    # permite diferenciar errores de "development", "staging" o "production".
    environment="development",
)


```
GlitchTip, usa el puerto "8000", por lo cual, el proyecto en django se debe de arrancar,
en el puerto "8001".


