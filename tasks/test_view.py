## Módulo: test_view.py
## Descripción: Contiene pruebas automatizadas para validar el
##              correcto funcionamiento de las vistas principales
##              de la aplicación de tareas: listado, creación y
##              eliminación de tareas.
## Fecha de creación: 2025/Noviembre/14
## Autor: GH (Gustavo Hernández)
## Fecha de última modificación: 2025/Noviembre/14
## Autor última modificación: GH
## Comentarios de última modificación: Se agregaron casos de
##              prueba, documentación y estructura siguiendo la guía
##              de legibilidad del proyecto.


from django.test import TestCase
from django.urls import reverse
from .models import Task

# Clase que agrupa las pruebas automatizadas para las vistas de Task
class TaskViewTests(TestCase):

    def test_task_list_view(self):
        """
        Caso 1: La vista de listado debe regresar 200.
        Validamos que la URL de lista funcione y cargue la plantilla correcta.
        """
        # Realiza una petición GET a la vista 'task-list'
        response = self.client.get(reverse('task-list'))

        # Verifica que la respuesta sea 200 OK
        self.assertEqual(response.status_code, 200)

        # Verifica que se haya renderizado el template correcto
        self.assertTemplateUsed(response, "tasks/task_list.html")

    def test_create_task(self):
        """
        Caso 2: Crear una tarea debe guardarla en la base de datos.
        Probamos que un POST cree correctamente una nueva tarea.
        """
        # Datos que se enviarán al formulario
        data = {
            "title": "Tarea de prueba",
            "description": "Probando creación",
            "status": "PENDIENTE"
        }

        # Enviar los datos mediante POST a la URL 'task-create'
        response = self.client.post(reverse('task-create'), data)

        # Después de crear, la vista debe redirigir (código 302)
        self.assertEqual(response.status_code, 302)

        # Validamos que ahora exista una tarea en la base
        self.assertEqual(Task.objects.count(), 1)

        # Verificamos que la tarea creada tenga el título correcto
        self.assertEqual(Task.objects.first().title, "Tarea de prueba")

    def test_delete_task(self):
        """
        Caso 3: Eliminar una tarea existente.
        Probamos que una tarea se elimine correctamente desde la vista.
        """
        # Crear una tarea temporal que luego será eliminada
        task = Task.objects.create(
            title="Eliminar",
            description="Tarea a eliminar",
            status="PENDIENTE"
        )

        # Enviar POST a la vista de eliminar tarea
        response = self.client.post(reverse('task-delete', args=[task.id]))

        # La vista debe redirigir después de eliminar (código 302)
        self.assertEqual(response.status_code, 302)

        # Validamos que ya no exista ninguna tarea en la BD
        self.assertEqual(Task.objects.count(), 0)
