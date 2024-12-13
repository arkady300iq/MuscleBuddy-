from django.urls import path 
from useful_materials import views

urlpatterns = [
    path('useful_materials/', views.useful_materials_view, name='useful_materials')
]