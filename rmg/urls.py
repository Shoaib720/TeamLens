from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>/', views.delete_profile_allocation, name='delete'),
    path('edit/<int:pk>/', views.edit_profile_allocation, name='edit'),
]