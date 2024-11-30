from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from workout.models import Preferences
from workout_plan.models import TrainingPlan
from workout.forms import PreferencesForm

@login_required
def preferences_view(request):
    if hasattr(request.user, 'preferences') and request.user.preferences.plan:
        return redirect('training_plan', plan_id=request.user.preferences.plan.id)

    if request.method == 'POST':
        form = PreferencesForm(request.POST)
        if form.is_valid():
            preferences, created = Preferences.objects.get_or_create(user=request.user)
            preferences.gender = form.cleaned_data['gender']
            preferences.experience = form.cleaned_data['experience']
            preferences.intensity = form.cleaned_data['intensity']

            if not preferences.plan:
                preferences.plan = TrainingPlan.objects.first()  

            preferences.save()
            return redirect('training_plan', plan_id=preferences.plan.id)
    else:
        form = PreferencesForm()

    return render(request, 'workouts/preferences.html', {'form': form})



@login_required
def create_workout_view(request):
    return render(request, 'workout_plan/training_plan.html')


