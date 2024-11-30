from django.shortcuts import render, get_object_or_404
from workout_plan.models import TrainingPlan, TrainingDay

def training_plan_view(request, plan_id):
    training_plan = get_object_or_404(TrainingPlan, id=plan_id)
    training_days = TrainingDay.objects.filter(training_plan=training_plan)
    return render(request, 'workout_plan/training_plan.html', {'training_plan': training_plan, 'training_days': training_days})

def training_day_detail_view(request, day_id):
    training_day = get_object_or_404(TrainingDay, id=day_id)
    return render(request, 'workout_plan/training_day_detail.html', {'training_day': training_day})
