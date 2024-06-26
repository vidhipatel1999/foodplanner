from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Restriction(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restrictions_detail', kwargs={'pk': self.id})
    
class Week(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    total_calorie_goal = models.IntegerField()
    notes = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restrictions = models.ManyToManyField(Restriction)

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