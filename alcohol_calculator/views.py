# alcohol_calculator/views.py
from django.shortcuts import render
from .forms import AlcoholForm


def calculate_alcohol(request):
    total_alcohol = None
    if request.method == 'POST':
        form = AlcoholForm(request.POST)
        if form.is_valid():
            total_alcohol = 0
            for i in range(1, 6):
                alcohol_percentage = form.cleaned_data.get(
                    f'alcohol_percentage_{i}')
                volume_ml = form.cleaned_data.get(f'volume_ml_{i}')
                total_alcohol += (alcohol_percentage * volume_ml) / 100
    else:
        form = AlcoholForm()
    return render(request, 'alcohol_calculator/calculate_form.html', {'form': form, 'total_alcohol': total_alcohol})
