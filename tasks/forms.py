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
        model = Task # Modelo con el que se generará el formulario
        fields = "__all__" # Se incluyen todos los campos del modelo

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


    
