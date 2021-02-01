from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    # password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password*'}))
    # password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation*'}))
    class Meta:
        model = User
        fields =['first_name', 'last_name','username', 'email', 'password1', 'password2']

