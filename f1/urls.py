from django.urls import path, include
from f1 import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', views.home, name='home'),
    path('add_driver/', views.add_driver, name='add_driver'),
    path('users/<int:user_id>/drivers/', views.driver_by_user, name='driver_by_user'),
    path('drivers/<int:pk>/update/', views.update_driver, name='update_driver'),
    path('drivers/<int:pk>/delete/', views.delete_driver, name='driver_confirmation_delete'),

]