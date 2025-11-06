#Modelo simple de una lista
#Se crea un modelo de una lista, en donde se pone en practica lo aprendido de vistas por clases.

from django.db import models

#Campos del modelo
class Task(models.Model):
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

