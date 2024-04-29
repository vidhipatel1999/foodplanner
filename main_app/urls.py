from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('accounts/logout/', views.logout_view, name='logout'),
]