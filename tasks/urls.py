from django.urls import path
# importing views from views..py
from .views import TaskCreate
urlpatterns = [
    path('', TaskCreate.as_view() ),
]
