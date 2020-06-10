from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Job, Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
def __init__(self, *args, **kwargs):
    self.helper.form_show_labels = False


class CreateAdminForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CreateEmployerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    

class AddJobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'