from django.urls import path
from workout import views

urlpatterns = [
    path('preferences/', views.preferences_view, name='preferences'),
    path('create_workout/', views.create_workout_view, name='create_workout'),
]
