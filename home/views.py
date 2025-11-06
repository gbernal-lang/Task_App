
from .models import Task

from django.views.generic import ListView
class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"
