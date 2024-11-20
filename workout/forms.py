from django import forms
from workout.models import Preferences

class PreferencesForm(forms.ModelForm):
    class Meta:
        model = Preferences
        fields = ['gender', 'experience', 'intensity']
        widgets = {
            'gender': forms.Select(attrs={'class': 'custom-select'}),
            'exprerience': forms.Select(attrs={'class': 'custom-select'}),
            'intensity': forms.Select(attrs={'class': 'custom-select'}),
        }
        labels = {
            'gender': 'Gender', 
            'experience': 'Training Experience',
            'intensity' : 'Workout Intensity'
        }

