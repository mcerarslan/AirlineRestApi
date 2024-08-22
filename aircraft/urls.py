from django.urls import path
from . import views

urlpatterns = [
    path('', views.aircrafts),
    path('<int:id>', views.aircraft),
]