from django.urls import path 
from main_page.views import main_page

urlpatterns = [
    path('', main_page, name='main_page'),
]

