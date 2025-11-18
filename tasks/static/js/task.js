/********************************************************************************************
 * Archivo: task.js
 * Descripción: Archivo JavaScript principal del proyecto.  
 *              Gestiona la validación dinámica de formularios y el filtrado interactivo  
 *              de tareas sin recargar la página. Incluye integración con SweetAlert  
 *              para mostrar alertas amigables al usuario.
 * 
 * Fecha de creación: 2025/Noviembre/14
 * Autor: GH (Gustavo Hernández)
 * 
 * Fecha de última modificación: 2025/Noviembre/14
 * Autor última modificación: GH
 * Comentarios de última modificación:
 *      - Se añadió validación dinámica del formulario con DOMContentLoaded.
 *      - Se implementó el filtrado en tiempo real de tareas usando dataset.
 *      - Se integró SweetAlert para mejorar la experiencia del usuario.
 *      - Se integra la función fetch
 ********************************************************************************************/


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