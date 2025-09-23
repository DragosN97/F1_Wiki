import json

from django.contrib.gis.shortcuts import render_to_kml
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import datetime

from pandas.io.formats.format import return_docstring
from rest_framework.generics import get_object_or_404

from f1.models import models
from f1.models import Driver
from f1.forms import DriverForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from f1.serializers import DriverSerializer
from rest_framework import viewsets
from django.contrib import messages

def main(request):
    return render(request, 'main.html', {"message": "This is the main page for F1 Drivers Wiki"})

def home(request):

    sort_by = request.GET.get('sort_by', 'name')

    if sort_by == 'date':
        drivers = Driver.objects.all().order_by('date_created').reverse()
    else:
        drivers = Driver.objects.all().order_by('name')

    context = {

        'username': request.user.username if request.user.is_authenticated else '',
        'logged_in': request.user.is_authenticated,
        'current_time': datetime.now(),
        'drivers': drivers,
        'sort_by': sort_by

    }

    return render(request, 'home.html', context)

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

def driver_by_user(request, user_id: int):
    '''Driver list sorted by user.'''
    drivers = list(Driver.objects.filter(created_by=user_id))
    drivers.sort(key=(lambda x: x.date_created), reverse=True)
    context = {
        'drivers': drivers
    }
    return render(request, 'drivers.html', context)


@login_required()
def add_driver(request):
    '''Add a driver method.'''
    if request.method == "GET":
        context = {
            'form': DriverForm()
        }
        return render(request, 'add_driver.html', context)

    elif request.method == "POST":
        form_data = DriverForm(request.POST, request.FILES)
        if form_data.is_valid():
            driver_instance = form_data.save(commit=False)
            driver_instance.created_by = request.user
            driver_instance.save()
            return redirect('home')
        else:
            return HttpResponse(form_data.errors)

@login_required
def delete_driver(request, pk):
    '''Delete a driver method'''
    driver = get_object_or_404(Driver, pk=pk)
    context = {
        'driver': driver,
        'message': 'This is not your driver'
    }
    # If someone try to delete another driver:
    if driver.created_by != request.user:
        return render(request, 'driver_error_delete.html', context)

    # If it's the same user:
    if request.method == "POST":
        driver.delete()
        return redirect('home')
    else:
        return render(request, 'driver_confirmation_delete.html', {'driver': driver})


def driver_detail(request, pk):
    '''Driver page with all the details'''
    if request.method == "GET":
        driver = get_object_or_404(Driver, pk=pk)
        context = {
            'driver': driver
        }
        return render(request, 'driver_detail.html', context)

@login_required
def update_driver(request, pk):
    '''Update or modify the driver method'''
    driver = get_object_or_404(Driver, pk=pk)
    context = {
        'driver': driver,
        'message': "You can't edit this Driver. It's not yours."
    }
    # If someone try to delete another driver:
    if driver.created_by != request.user:
        return render(request, 'driver_error_delete.html', context)
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES, instance=driver)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = DriverForm(instance=driver)
        return render(request, 'update_driver.html', {'form': form, 'driver': driver})











