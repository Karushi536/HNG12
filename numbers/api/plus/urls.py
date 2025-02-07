from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.classify_number, name='classify_number'),
]