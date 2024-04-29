from django.db import models

# Create your models here.
class Week(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    total_calorie_goal = models.IntegerField()
    notes = models.TextField(max_length=250)  