from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import View
from django import forms
from django.urls import reverse
from django.shortcuts import render
from .forms import *
from .models import *
from .cart import Cart
from django.http import JsonResponse


# Create your views here.

class homePageView(TemplateView):
    template_name = 'core/home.html'

def loginPageView(request):
    if request.method=="POST":
        email = request.POST["email"]
        password = request.POST["password1"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Ha iniciado sesión correctamente"))
            return redirect('home')
        else:
            messages.success(request, ("Hubo un error"))
            return redirect('login')
    else:
        return render(request, 'user/login.html', {})

def logoutPageView(request):
    logout(request)
    messages.success(request,(" Ha cerrado sesión exitosamente"))
    return redirect('home')


def singupView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST["email"]
            password = request.POST["password1"]
            # Log in user
            user = authenticate(request, email=email, password=password)
            login(request, user)
            messages.success(request, "Has creado la cuenta exitosamente")
            return redirect('home')
        else:
            messages.error(request, "Hubo un error al procesar el formulario.")
    else:
        form = SignUpForm()

    return render(request, 'user/singup.html', {'form': form})


def productsPageView(request):
    products = Product.objects.all()
    return render(request, 'core/productsM.html', {'products': products})

def singlePageView(request,pk):
    product=Product.objects.get(id=pk)
    return render(request, 'core/single.html', {'product':product})


def cartResumePageView(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request, 'cart/cartR.html', {"cart_products": cart_products, "quantities":quantities})

def cartAddPageView(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity = product_quantity)
        cart_quantity = cart.__len__()
        response= JsonResponse({'qty': cart_quantity})
        #response= JsonResponse({'Product Name': product.name})
        return response

def cartDeletePageView(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response= JsonResponse({'product': product_id})
        return response
    
def cartUpdatePageView(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, quantity= product_qty)
        response= JsonResponse({'qty': product_qty})
        return response
        #return redirect('cart/cartR.html')