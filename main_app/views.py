from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Week, Restriction
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
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
    id_list = week.restrictions.all().values_list('id')
    restrictions_that_week_doesnt_have = Restriction.objects.exclude(id__in=id_list)

    meal_form = MealForm()
    now = datetime.now()  # Getting the current date and time
    return render(request, 'weeks/detail.html', {
        'week': week,
        'meal_form': meal_form,
        'now': now,
        'restrictions': restrictions_that_week_doesnt_have
    })

@login_required
def add_meal(request, week_id):
    # access form field input values
    submitted_form = MealForm(request.POST) # this creates django's version of req.body
    # validate form input
    if submitted_form.is_valid():
        new_meal = submitted_form.save(commit=False) # commit=false ensures it doesn't save to the database
        new_meal.week_id = week_id
        new_meal.save()
    return redirect('detail', week_id=week_id)

@login_required
def assoc_restriction(request, week_id, restriction_id):
    Week.objects.get(id=week_id).restrictions.add(restriction_id)
    return redirect('detail', week_id=week_id)

@login_required
def unassoc_restriction(request, week_id, restriction_id):
    Week.objects.get(id=week_id).restrictions.remove(restriction_id)
    return redirect('detail', week_id=week_id)

@login_required
def update_restrictions(request, week_id):
    week = Week.objects.get(id=week_id)
    if request.method == 'POST':
        current_restrictions_ids = set(week.restrictions.all().values_list('id', flat=True))
        selected_restrictions_ids = set(int(id) for id in request.POST.getlist('restrictions'))

        # Finding restrictions to add (newly checked) and to remove (unchecked)
        to_add = selected_restrictions_ids - current_restrictions_ids
        to_remove = current_restrictions_ids - selected_restrictions_ids

        # Updating the week's restrictions based on the changes
        week.restrictions.remove(*to_remove)
        week.restrictions.add(*to_add)

        return redirect('detail', week_id=week_id)
    else:
        # If not a POST request, redirect back to the detail page or handle accordingly
        return redirect('detail', week_id=week_id)

class WeekCreate(LoginRequiredMixin, CreateView):
    model = Week
    fields = ['start_date', 'end_date', 'total_calorie_goal', 'notes']

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class WeekUpdate(LoginRequiredMixin, UpdateView):
    model = Week
    fields = ['start_date', 'end_date', 'total_calorie_goal', 'notes']

class WeekDelete(LoginRequiredMixin, DeleteView):
    model = Week
    success_url = '/weeks/'

class RestrictionList(LoginRequiredMixin, ListView):
    model = Restriction

class RestrictionDetail(LoginRequiredMixin, DetailView):
    model = Restriction

class RestrictionCreate(LoginRequiredMixin, CreateView):
  model = Restriction
  fields = '__all__'

class RestrictionUpdate(LoginRequiredMixin, UpdateView):
  model = Restriction
  fields = '__all__'

class RestrictionDelete(LoginRequiredMixin, DeleteView):
  model = Restriction
  success_url = '/restrictions'