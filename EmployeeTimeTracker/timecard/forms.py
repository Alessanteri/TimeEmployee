from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class DailyLogForm(ModelForm):
    class Meta:
        model = DailyLog
        fields = '__all__'


class ObjectForm(ModelForm):
    class Meta:
        model = ObjectName
        fields = '__all__'


class MessageForm(ModelForm):
    class Meta:
        model = MessageObject
        fields = '__all__'
