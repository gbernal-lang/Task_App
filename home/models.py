#Modelo simple de una lista
#Se crea un modelo de una lista, en donde se pone en practica lo aprendido de vistas por clases.

from django.db import models

#se declara un nuevo modelo con nombre Task
class Task(models.Model):
    class Meta:
        verbose_name="Nombre de tareas"
    #Campos del modelo
    titulo = models.CharField(max_length=200,verbose_name="Tareas")
    descripcion = models.CharField(verbose_name="Descripcion de tarea",blank=True,null=True)

    def __str__(self):
         return f"{self.titulo} {self.descripcion}"
