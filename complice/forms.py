from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Goal



class Goal_form(forms.ModelForm):
    class Meta:
        model = Goal
        exclude = ('created_date','author')