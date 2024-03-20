from .models import *
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
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'availability_xs', 'availability_s', 'availability_m', 'availability_l', 'availability_xl', 'image', 'gender', 'is_sale', 'sale_price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'availability_xs': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Cantidad en talla XS'}),
            'availability_s': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Cantidad en talla S'}),
            'availability_m': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Cantidad en talla M'}),
            'availability_l': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Cantidad en talla L'}),
            'availability_xl': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Cantidad en talla XL'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'is_sale': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sale_price': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Precio En Descuento', 'required': False}),
        }