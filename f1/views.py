import json

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from f1.models import models
from f1.models import Driver
from f1.forms import DriverForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from f1.serializers import DriverSerializer
from rest_framework import viewsets

def main(request):
    return render(request, 'main.html', {"message": "This is the main page for F1 Drivers Wiki"})

def home(request):

    drivers = list(Driver.objects.all())
    drivers.sort(key=(lambda x: x.date_created), reverse=True)

    context = {

        'username': request.user.username if request.user.is_authenticated else '',
        'logged_in': request.user.is_authenticated,
        'current_time': datetime.now(),
        'drivers': drivers,

    }

    return render(request, 'home.html', context)

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


@csrf_exempt
@login_required()
def add_driver(request):
    if request.method == "GET":
        context = {
            'form': DriverForm()
        }
        return render(request, 'add_driver.html', context)

    elif request.method == "POST":
        form_data = DriverForm(request.POST)
        if form_data.is_valid():
            driver_instance = form_data.save(commit=False)
            driver_instance.created_by = request.user
            driver_instance.save()
            return redirect('drivers')
        else:
            return HttpResponse(form_data.errors)

def driver_by_user(request, user_id: int):
    drivers = list(Driver.objects.filter(created_by=user_id))
    drivers.sort(key=(lambda x: x.date_created), reverse=True)
    context = {
        'drivers': drivers
    }
    return render(request, 'drivers.html', context)






