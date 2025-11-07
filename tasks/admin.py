from django.contrib import admin

#se importa el modelo de Task al panel de administradorpython manage.py createsuperuser
from .models import Task

admin.site.register(Task)