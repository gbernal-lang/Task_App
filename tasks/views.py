from django.views.generic.edit import CreateView
from .models import Task

class TaskCreate(CreateView):

    # specify the model for create view
    model = Task
    template_name = "task_view.html" #nombre del template en html

    # specify the fields to be displayed
    fields = ['title', 'description','status']