from django.contrib import admin
from .models import Week, Meal
# Register your models here.
admin.site.register([Week, Meal])