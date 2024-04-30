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
    
class Meal(models.Model):
    MEALS = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner')
    )
    date = models.DateField('meal date')
    meal = models.CharField(max_length=1, choices=MEALS, default='B')
    name = models.CharField(max_length=100)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}' 
    
    class Meta:
        ordering = ('-date',)  
