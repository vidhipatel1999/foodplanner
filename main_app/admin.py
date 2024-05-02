from django.contrib import admin
from .models import Week, Meal, Restriction
# Register your models here.
admin.site.register([Week, Meal, Restriction])