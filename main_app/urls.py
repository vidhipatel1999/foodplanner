from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/signup/', views.signup, name='signup'),
    path('weeks/', views.weeks_index, name='index'),
    path('weeks/<int:week_id>/', views.weeks_detail, name='detail'),
    path('weeks/create/', views.WeekCreate.as_view(), name='weeks_create'),
    path('weeks/<int:pk>/update/', views.WeekUpdate.as_view(), name='weeks_update'),
    path('weeks/<int:pk>/delete/', views.WeekDelete.as_view(), name='weeks_delete'),
    path('weeks/<int:week_id>/add_meal/', views.add_meal, name='add_meal')
]