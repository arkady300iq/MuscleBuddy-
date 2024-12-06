from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from workout.models import Preferences
from workout_plan.models import TrainingPlan
from workout.forms import PreferencesForm

@login_required
def preferences_view(request):
    preferences = getattr(request.user, 'preferences', None)
    if preferences and preferences.plan:
        if request.GET.get('return_to_preferences'):
            pass 
        else:
            return redirect('training_plan', plan_id=preferences.plan.id)

    if request.method == 'POST':
        form = PreferencesForm(request.POST)
        if form.is_valid():
            preferences, created = Preferences.objects.get_or_create(user=request.user)
            preferences.gender = form.cleaned_data['gender']
            preferences.experience = form.cleaned_data['experience']
            preferences.intensity = form.cleaned_data['intensity']

            training_plan = TrainingPlan.objects.filter(
                gender=preferences.gender,
                experience=preferences.experience,
                intensity=preferences.intensity).first()

            preferences.plan = training_plan 
            preferences.save()

            if training_plan:
                return redirect('training_plan', plan_id=training_plan.id)
            else:
                return render(request, 'workout_plan/no_plan.html')
    else:
        form = PreferencesForm()

        

    return render(request, 'workouts/preferences.html', {'form': form})







@login_required
def create_workout_view(request):
    return render(request, 'workout_plan/training_plan.html')


