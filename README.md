Documentacion de la aplicación "Task App"

Gestor de tareas desarrollado con Django utilizando Vistas Basadas en Clases (Class-Based Views). Este proyecto está orientado al aprendizaje estructurado del flujo de trabajo con Git, manejo de ramas y buenas prácticas de desarrollo.

*Características del Proyecto

->Crear tareas

->Editar tareas

->Eliminar tareas

->Listar tareas

->Sistema de mensajes de confirmación

*Tecnologías Utilizadas

->Python 3.10.9

->Django 5

->SQLite (base de datos por defecto)

->HTML + CSS

*Instalación

->Clonar el repositorio:
git clone https://github.com/usuario/Task_App.git
cd Task_App

->Crear y activar el entorno virtual:

python -m venv venv
source venv/Scripts/activate  # Windows

->Instalar dependencias:

pip install -r requirements.txt

->Aplicar migraciones:

python manage.py migrate

->Url para ver el entorno virtual

http://127.0.0.1:8000/

*Flujo de Trabajo con Git

Ramas
Rama	          Propósito
->main	          Rama principal estable
->modeltask	      Rama base del módulo de tareas
->create-task	  Implementación de creación de tareas
->delete-task	  Implementación de eliminación de tareas
->update-task	  Implementación de actualización de tareas


*Proceso de Integración

->Crear una rama desde main

->Desarrollar la funcionalidad

->Hacer commit con mensajes claros

->Hacer merge (resolviendo conflictos si existen)

->Finalmente, hacer squash merge de modeltask → main


*Evidencia

Se creó una carpeta llamada evidencia dentro de static/ donde se almacenan las capturas de pantalla del funcionamiento del proyecto.

tasks\static\evidencia\Evidencia_Crear Tareas.jpg
tasks\static\evidencia\Evidencia_Editar Tareas.jpg
tasks\static\evidencia\Evidencia_Eliminar Tareas.jpg
tasks\static\evidencia\Evidencia_Lista de Tareas.jpg

Estas imágenes muestran el correcto funcionamiento de cada vista (List, Create, Update, Delete).


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*Descripción del proyecto en General.

Proyecto creado como parte del aprendizaje de flujo Git y Django.

*Flujo Git Real Utilizado

Este es el flujo de desarrollo que se siguió durante el proyecto:

*Configuración Inicial

->Creación de entorno virtual.

->Instalación de Django.

->Creación de la app home como prueba inicial.

*Configuración del Repositorio

->Clonación del repositorio remoto.

->Configuración de archivo .env.

->Levantamiento del servidor para verificar funcionamiento.

*Ramas y Flujo de Trabajo

->Creación de rama feature/gustavo para primeras pruebas y Pull Request.

->Creación de rama Aprender_CBV para practicar y aprender Vistas Basadas en Clases.

->Creación de rama modeltask donde se creó la app tasks y el modelo Task.

*Implementación por Funcionalidades

->Rama feature/create-task para implementar CreateView.

->Rama feature/delete-task para implementar DeleteView + confirmación.

->Rama feature/update-task para implementar UpdateView.

*Integración Final

->Las ramas feature/create-task, feature/delete-task y feature/update-task no tuvieron Pull Request.

->En su lugar, estas ramas se integraron primero en modeltask usando merge.

->Después, la rama modeltask se integró a main utilizando Squash & Merge para mantener el historial limpio.

->Finalmente, se actualizó main en el repositorio remoto con git push.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Conexión de Django con PostgreSQL y exploración en DBeaver

## Descripción general
Este documento describe el proceso realizado para conectar un proyecto Django con una base de datos PostgreSQL, ejecutar las migraciones necesarias y explorar los esquemas, tablas y registros utilizando pgadmin.

El proyecto utilizado fue **Task App**, una aplicación para gestionar tareas con vistas basadas en clases (CBV).

---

## Configuración de la conexión a la base de datos

En el archivo `settings.py` del proyecto Django, se configuró la conexión de la siguiente manera:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'task_app',
        'USER': 'dev_user',
        'PASSWORD': 'Dev2025',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
