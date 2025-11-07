from django.db import models
#Modelo con los campos solicitados
class Task (models.Model):

  #Campos del modelo
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    created_at = models.CharField(max_length=100)
    updated_at = models.CharField(max_length=100)


    def __str__(self):
        return self.titulo   
