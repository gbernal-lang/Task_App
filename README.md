#  Integrar interactividad con JavaScript en Django

Para esta actividad, en primer lugar, se creo un platilla principal llamada "base.html", esto para, 
no duplicar codigo en cada vista.

### base.html

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

Después, se creó el archivo Js llamado "task.js", en este se encuentra las funciones para validar que no se envie el formulario si tiene campos vacios,
tambien, pára hacer un filtro de tareas y finalmente la función para hacer una petición fetch.

### task.js

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
Después, se creó una nueva vista basada en funciones con el propósito de exponer la cantidad total de tareas registradas en la base de datos.
Esta vista retorna los datos en formato JSON, lo que permite su consumo mediante fetch en el frontend.

### view.py 

```bash
def task_count(request):
    # Obtiene la cantidad total de registros almacenados en el modelo Task
    count = Task.objects.count()
    # Retorna la respuesta en formato JSON con la clave 'total'
    return JsonResponse ({"total":count})
```

Finalmente se agregar una url, apuntando a la función con petición fetch, asi mismo, en task_list.html se se agrega la barra de busqueda para filtrar tareas
y una etiqueta para ver el numero de tareas sin recargar la pagina.

### url.py

```bash
    #Endpoint que permite obtener el número total de tareas registradas
    # Este endpoint es consumido mediante la función fetch
    # y retorna un JSON con el conteo total de registros del modelo Task.

    path("task-count/", task_count, name="task-count")
```

### task_list.html

```bash
 <!-- Campo de búsqueda -->
  <input type="text" id="filtro" placeholder="Buscar tareas..." class="search-input">

  <!-- Etiqueta para contador -->
  <p class="task-count">Total de tareas: <span id="total-tasks">0</span></p>

   <tbody id="task-table-body">
      {% for task in tasks %}
    <!--
      {# 
        Cada fila <tr> representa una tarea.
        - data-title: guarda el título de la tarea
        - data-description: guarda la descripción
        Estos atributos "data-*" permiten que el JS pueda leerlos para filtrar sin recargar la página.
    #}
      -->
     <tr data-title="{{ task.title }}" data-description="{{ task.description }}">

```
