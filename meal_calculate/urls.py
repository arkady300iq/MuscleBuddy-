from django.urls import path
from meal_calculate import views

urlpatterns = [
    path('nutrition_calculator/', views.nutrition_calculator_view, name ='nutrition_calculator'),
    path('nutrition_result/', views.nutrition_result_view, name='nutrition_result'),
]