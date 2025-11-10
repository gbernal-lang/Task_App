Para esta actividad se creó una vista basada en clases utilizando DeleteView.
En esta vista se especificó el modelo correspondiente y la URL a la que se redirige después de eliminar el registro. Además, se agregó un mensaje de confirmación para informar al usuario que la tarea fue eliminada correctamente.

También se creó una vista basada en función (index) para usarla como página de prueba y como destino de redirección una vez que la eliminación se haya completado.

Finalmente, se agregaron las rutas necesarias en el archivo urls.py, incluyendo la ruta que recibe el identificador de la tarea (pk) para poder eliminar el registro seleccionado.