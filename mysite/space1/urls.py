from django.urls import path
from . import views

urlpatterns = [
    path('random_apod/', views.random_apod, name='random_apod'),
]
