from django.urls import path
from . import views

urlpatterns = [
    path('', views.airline_list),
    path('<int:id>', views.airline),
    path('create/', views.airline_create),
    path('update/<int:id>', views.airline_update),
    path('patch/<int:id>', views.airline_patch),
    path('delete/<int:id>', views.airline_delete)
]