from django.db import models
from django.urls import reverse

# Create your models here.
class Week(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    total_calorie_goal = models.IntegerField()
    notes = models.TextField(max_length=250)  

    def __str__(self):
        return f"Week from {self.start_date} to {self.end_date}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'week_id': self.id})