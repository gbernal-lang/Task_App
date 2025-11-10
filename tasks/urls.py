from django.urls import path
from . import views
from .views import TaskUpdate

urlpatterns = [
    path('', views.index, name='tasks_index'),
    path('edit/<int:pk>/', TaskUpdate.as_view(), name='task-update'),

]
