from django.urls import path
from . import views

urlpatterns = [
    path('', views.airlines),
    path('<int:id>', views.airline),
]