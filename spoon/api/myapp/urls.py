from .views import my_model_view
from django.urls import path

urlpatterns = [
    path('api/', my_model_view)
]