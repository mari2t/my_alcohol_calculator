# alcohol/forms.py

from django import forms
from .models import Drink, DailyGoal


class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ['date', 'name', 'volume', 'alcohol_percentage']


class DailyGoalForm(forms.ModelForm):
    class Meta:
        model = DailyGoal
        fields = ['date', 'goal']
