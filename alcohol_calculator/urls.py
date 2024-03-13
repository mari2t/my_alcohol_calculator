
from django.urls import path
from .views import calculate_alcohol

urlpatterns = [
    path('calculate/', calculate_alcohol, name='calculate_alcohol'),
]
