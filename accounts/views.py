from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from accounts.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def registration_view(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    return render(request, 'login.html', {'form': form})