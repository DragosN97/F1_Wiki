from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Driver(models.Model):
    name = models.CharField(max_length=255)
    team = models.CharField(max_length=255)
    age = models.IntegerField()
    about = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='f1')
    date_created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='driver_image/', blank=True, null=True)

# def __str__(self):
#     return f'Name: {self.name} Team: {self.team} Age: {self.age}'

class Like(models.Model):
    user_like = models.ForeignKey(User, on_delete=models.CASCADE)
    driver_like = models.ForeignKey(Driver, on_delete=models.CASCADE)