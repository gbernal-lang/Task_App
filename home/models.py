#Modelo simple de una lista
#Se crea un modelo de una lista, en donde se pone en practica lo aprendido de vistas por clases.

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
