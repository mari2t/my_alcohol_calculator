# alcohol/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Drink, DailyGoal
from .forms import DrinkForm, DailyGoalForm


class DrinkListView(ListView):
    model = Drink
    context_object_name = 'drinks'
    template_name = 'alcohol/drink_list.html'


class DrinkCreateView(CreateView):
    model = Drink
    form_class = DrinkForm
    success_url = reverse_lazy('drink_list')
    template_name = 'alcohol/drink_form.html'


class DrinkUpdateView(UpdateView):
    model = Drink
    form_class = DrinkForm
    success_url = reverse_lazy('drink_list')
    template_name = 'alcohol/drink_form.html'


class DrinkDeleteView(DeleteView):
    model = Drink
    success_url = reverse_lazy('drink_list')
    template_name = 'alcohol/drink_confirm_delete.html'


def daily_goal_view(request):
    if request.method == 'POST':
        form = DailyGoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drink_list')
    else:
        form = DailyGoalForm()
    return render(request, 'alcohol/daily_goal.html', {'form': form})
