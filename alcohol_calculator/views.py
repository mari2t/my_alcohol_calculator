from django.shortcuts import render
from .forms import AlcoholForm


def calculate_alcohol(request):
    if request.method == 'POST':
        form = AlcoholForm(request.POST)
        if form.is_valid():
            total_alcohol = 0
            for i in range(1, 6):
                alcohol_percentage = form.cleaned_data[f'alcohol_percentage_{i}']
                volume_ml = form.cleaned_data[f'volume_ml_{i}']
                # アルコールの総量を計算
                total_alcohol += (alcohol_percentage * volume_ml) / 100

            return render(request, 'result.html', {'total_alcohol': total_alcohol, 'form': form})
    else:
        form = AlcoholForm()
    return render(request, 'alcohol_form.html', {'form': form})
