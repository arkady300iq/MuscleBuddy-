from django import forms
from meal_calculate.models import MealCalculation

class NutritionForm(forms.ModelForm):
    class Meta:
        model = MealCalculation
        fields =['weight', 'gender', 'goal', 'activity_level']
        widgets = {
            'weight': forms.NumberInput(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'goal': forms.Select(attrs={'class':'form-control'}),
            'activity_level': forms.Select(attrs={'class': 'form-control'}),
        }