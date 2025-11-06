from django.http import HttpResponse

def homeView(request):
    return HttpResponse("Vista djangoo")

from django.views.generic import ListView
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"
