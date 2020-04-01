from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisForm(UserCreationForm):
	email = forms.EmailField(required=True) #here we giving "required=True" means making Email field mandatory to fill to register
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]