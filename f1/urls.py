from django.urls import path, include
from f1 import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', views.home, name='home'),
    path('add_driver/', views.add_driver, name='add_driver'),
]