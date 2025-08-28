from django import forms
from f1.models import Driver

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'team', 'age', 'about']