###########################################################
## Módulo: forms.py (Formularios de la aplicación de tareas)
## Descripción: Define un formulario basado en el modelo Task
##              para crear y gestionar tareas desde la interfaz web.
## Fecha de creación: 2025/Noviembre/11
## Autor: GH (Gustavo Hernández)
## Fecha de última modificación: 2025/Noviembre/12
## Autor última modificación: GH
## Comentarios de última modificación: Se agregaron comentarios descriptivos
##              y estructura conforme a la guía de legibilidad.
###########################################################


# Se importa el módulo forms de Django, que permite crear formularios
from django import forms

# Se importa el modelo del archivo models.py
from .models import Task


# Creamos un ModelForm basado en el modelo Task
class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task  # Modelo con el que se generará el formulario
        fields = "__all__"  # Se incluyen todos los campos del modelo
