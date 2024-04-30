from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Week
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

def weeks_index(request):
  weeks = Week.objects.all()
  return render(request, 'weeks/index.html', {
    'weeks': weeks
  })

def weeks_detail(request, week_id):
  week = Week.objects.get(id=week_id)
  return render(request, 'weeks/detail.html', {
    'week': week 
  })

class WeekCreate(CreateView):
    model = Week
    fields = '__all__'

class WeekUpdate(UpdateView):
    model = Week
    fields = '__all__'

class WeekDelete(DeleteView):
    model = Week
    success_url = '/weeks/'