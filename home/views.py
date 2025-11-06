from django.http import HttpResponse

def homeView(request):
    return HttpResponse("Vista djangoo")

from django.views.generic.base import ListView
class TaskListViewgit(ListView):
    template_name = "task_list.html"
