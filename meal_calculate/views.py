from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NutritionForm
from .models import MealCalculation
from .utils import calculate_nutrition  

@login_required
def nutrition_calculator_view(request):
    result = None 

    if request.method == 'POST':
        form = NutritionForm(request.POST)
        if form.is_valid():
            nutrition_calculate = form.save(commit=False)
            nutrition_calculate.user = request.user 
            result = calculate_nutrition(
                nutrition_calculate.weight, 
                nutrition_calculate.gender, 
                nutrition_calculate.goal,
                nutrition_calculate.activity_level 
            )

            nutrition_calculate.protein = result['protein']
            nutrition_calculate.fat = result['fat']
            nutrition_calculate.carbs = result['carbs']
            nutrition_calculate.save()

            return redirect('nutrition_result')  
    else:
        form = NutritionForm()

    return render(request, 'workouts/nutrition_calculator.html', {'form': form, 'result': result})


def nutrition_result_view(request):
    result = MealCalculation.objects.filter(user=request.user).order_by('-calculated_at').first()
    return render(request, 'workouts/result.html', {'result': result})