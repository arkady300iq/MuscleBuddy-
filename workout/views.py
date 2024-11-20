from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PreferencesForm

@login_required
def preferences_view(request):
    if hasattr(request.user, 'preferences'):
        return redirect('create_workout')  

   
    if request.method == 'POST':
        form = PreferencesForm(request.POST)
        if form.is_valid():
            preferences = form.save(commit=False)
            preferences.user = request.user 
            preferences.save()
            return redirect('create_workout') 
    else:
        form = PreferencesForm()  

    return render(request, 'workouts/preferences.html', {'form': form})


@login_required
def create_workout_view(request):
    return render(request, 'workouts/create_workout.html')