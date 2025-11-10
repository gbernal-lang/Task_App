# Se importa el módulo forms de Django, que permite crear formularios
from django import forms
 
# Se importa el modelo del archivo models.py
from .models import Task
 
# Creamos un ModelForm basado en el modelo Task
class TaskCreateForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Task # Modelo con el que se generará el formulario
        fields = "__all__" # Se incluyen todos los campos del modelo