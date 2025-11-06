from django.urls import path
from .views import homeView

urlpatterns = [
    path("", homeView, name='home')
]

from .views import TaskListView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
]
