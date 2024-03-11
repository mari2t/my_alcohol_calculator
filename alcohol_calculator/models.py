from django.db import models
from django.contrib.auth.models import User


class Drink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=100)
    volume = models.FloatField()  # ml単位
    alcohol_percentage = models.FloatField()  # アルコールパーセンテージ
    created_at = models.DateTimeField(auto_now_add=True)

    def alcohol_amount(self):
        return self.volume * (self.alcohol_percentage / 100.0)


class DailyGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    goal = models.FloatField()  # その日のアルコール摂取目標量（g）
