#Modelo simple de una lista
#Se crea un modelo de una lista, en donde se pone en practica lo aprendido de vistas por clases.

from django.db import models

#se declara un nuevo modelo con nombre Task
class Task(models.Model):
    #Campos del modelo
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(verbose_name="Descripcion de tarea",blank=True,null=True)

    def __str__(self):
        return self.titulo

