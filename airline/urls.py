from django.urls import path
from . import views

urlpatterns = [
    path('', views.airline_list),
    path('create/', views.airline_create)
]