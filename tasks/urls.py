from django.urls import path
# importing views from views..py
from .views import TaskCreate
urlpatterns = [
    #Se agrega un nombre para identificar la url
    path('', TaskCreate.as_view(), name='task-create' ),
]
