from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'password1', 'password2' ) 

    def clean_email(self):
        email=self.cleaned_data['email'].lower()
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} no es valido')
    
    def clean_name(self):
        name=self.cleaned_data['name'].lower()
        try:
            user = User.objects.get(name=name)
        except Exception as e:
            return name
        raise forms.ValidationError(f'Email {name} no es valido')