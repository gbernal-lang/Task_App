from django.urls import path
from . import views
#Url para la vista basada en funciones
urlpatterns = [
    path('', views.index, name='tasks_index'),
]
