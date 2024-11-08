from django.urls import path
from user_profile.views import profile_view

urlpatterns = [
    path('<int:pk>/user_profile/', profile_view, name='user_profile')
]