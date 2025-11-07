from django.http import HttpResponse
#Vista basada en funciones, para verificar que se ve en el servidor local
def index(request):
    return HttpResponse("Gestor de tareas funcionando ✅")
