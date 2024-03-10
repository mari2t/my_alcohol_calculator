# alcohol_calculator/forms.py
from django import forms


class AlcoholForm(forms.Form):
    alcohol_percentage_1 = forms.DecimalField(
        label='アルコール度数 (%)', min_value=0, max_digits=5, decimal_places=2)
    volume_ml_1 = forms.DecimalField(
        label='ボリューム (ml)', min_value=0, max_digits=5, decimal_places=0)
    alcohol_percentage_2 = forms.DecimalField(
        label='アルコール度数 (%)', min_value=0, max_digits=5, decimal_places=2)
    volume_ml_2 = forms.DecimalField(
        label='ボリューム (ml)', min_value=0, max_digits=5, decimal_places=0)
    alcohol_percentage_3 = forms.DecimalField(
        label='アルコール度数 (%)', min_value=0, max_digits=5, decimal_places=2)
    volume_ml_3 = forms.DecimalField(
        label='ボリューム (ml)', min_value=0, max_digits=5, decimal_places=0)
    alcohol_percentage_4 = forms.DecimalField(
        label='アルコール度数 (%)', min_value=0, max_digits=5, decimal_places=2)
    volume_ml_4 = forms.DecimalField(
        label='ボリューム (ml)', min_value=0, max_digits=5, decimal_places=0)
    alcohol_percentage_5 = forms.DecimalField(
        label='アルコール度数 (%)', min_value=0, max_digits=5, decimal_places=2)
    volume_ml_5 = forms.DecimalField(
        label='ボリューム (ml)', min_value=0, max_digits=5, decimal_places=0)
