from django.urls import path
from .views import training_plan_view, training_day_detail_view

urlpatterns = [
    path('plan/<int:plan_id>/', training_plan_view, name='training_plan'),
    path('day/<int:day_id>/', training_day_detail_view, name='training_day_detail'),
]
