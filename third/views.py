from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Car
from .forms import CarForm

def authentication_test(request):
    template_name = 'registration/authentication_test.html'
    user = request.user
    context = {
        'user': user,
    }
    return render(request, template_name, context)


def create_user(request):
    template_name = 'registration/create_user.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('authentication_test')
    else:
        form = UserCreationForm()
    return render(request, template_name, {'form': form})

def car_view(request):
    template_name = 'cars.html'
    cars = Car.objects.all()

    if request.method == 'GET':
        form = CarForm()
        context = {
            'cars': cars,
            'form': form,
        }
        return render(request, template_name, context)
    
    elif request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {
                'cars': cars,
                'form': form,
            }
        return render(request, template_name, context)
            

