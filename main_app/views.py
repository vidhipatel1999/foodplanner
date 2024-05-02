from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Week
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import MealForm
from datetime import datetime

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def weeks_index(request):
  weeks = Week.objects.filter(user=request.user)
  return render(request, 'weeks/index.html', {
    'weeks': weeks
  })

@login_required
def weeks_detail(request, week_id):
    week = Week.objects.get(id=week_id)
    meal_form = MealForm()
    now = datetime.now()  # Get the current date and time
    return render(request, 'weeks/detail.html', {
        'week': week,
        'meal_form': meal_form,
        'now': now  # Pass the current datetime to the template
    })

@login_required
def add_meal(request, week_id):
    # access form field input values
    submitted_form = MealForm(request.POST) # this creates django's version of req.body
    # validate form input
    if submitted_form.is_valid():
        # if form input is valid, we'll save an in-memory copy of the new meal object
        new_meal = submitted_form.save(commit=False) # commit=false ensures it doesn't save to the database
        # attach the week id to the in-memory feeding object
        new_meal.week_id = week_id
        # save the completed meal object in the database
        new_meal.save()
        # redirect back to the week detail page
    return redirect('detail', week_id=week_id)

class WeekCreate(LoginRequiredMixin, CreateView):
    model = Week
    fields = ['start_date', 'end_date', 'total_calorie_goal', 'notes']

    def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)

class WeekUpdate(LoginRequiredMixin, UpdateView):
    model = Week
    fields = '__all__'

class WeekDelete(LoginRequiredMixin, DeleteView):
    model = Week
    success_url = '/weeks/'
