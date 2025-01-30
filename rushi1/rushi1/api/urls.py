from .views import MyModelview
from django.urls import path

urlpatterns = [
    path('api/',MyModelview)
]