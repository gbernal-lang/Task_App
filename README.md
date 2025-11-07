Se Creó una nueva aplicación llamada "tasks", en donde se creó un nuevo modelo llamado "Task", este modelo contiene los campos de title, description, status, created at, updated at.
Después, esto se ejecutaron los comandos de:

python manage.py makemigrations tasks
python manage.py migrate

Finalmente, este modelo se importó al archivo de "admin.py", después para verificar se ingresó a la url local con /admin, en donde se pudo verificar el modelo, con los campos solicitados en la tarea.