from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from. models import *



class LoginForm(forms.Form):
    username = forms.CharField( widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['name','address','city','country','date_of_birth','phone','gender','phone']
		