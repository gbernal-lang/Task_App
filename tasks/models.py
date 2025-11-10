from django.db import models
#Modelo con los campos solicitados
class Task (models.Model):
 

#Opciones para el campo de estatus
    ESTATUS_OPCIONES = [
        ("PENDIENTE", "Pendiente"),
        ("EN_PROCESO", "En proceso"),
        ("TERMINADO", "Terminado"),
    ]

  #Campos del modelo
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.CharField(max_length=200, verbose_name="Descripcion")
    status = models.CharField(max_length=200, verbose_name="Estatus", choices= ESTATUS_OPCIONES,default="pendiente")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado por:")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado por:")


    def __str__(self):
        return self.title

