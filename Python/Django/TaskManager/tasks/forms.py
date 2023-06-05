from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from . import models
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('completeDate', 'user')

class UserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']