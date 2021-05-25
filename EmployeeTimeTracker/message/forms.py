from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class MessageForm(ModelForm):
    class Meta:
        model = message
        fields = '__all__'


class FilterForm(forms.Form):
    FILTER_CHOICES = (
        ('time', 'Time'),
        ('timesince', 'Time Since'),
        ('timeuntil', 'Time Untill'),
    )

    filter_by = forms.ChoiceField(choices = FILTER_CHOICES)