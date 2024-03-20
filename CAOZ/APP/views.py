from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView


# Create your views here.

class homePageView(TemplateView):
    template_name = 'core/home.html'

def loginPageView(request):
    if request.method=="POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password1", "")
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
            pass
    else:
        form = SignUpForm()

    return render(request, 'user/singup.html', {'form': form})


def productsPageView(request):
    products = Product.objects.all().order_by('price')
    return render(request, 'core/products.html', {'products': products})

def productsMPageView(request):
    products = Product.objects.filter(gender='hombre')
    return render(request, 'core/productsM.html', {'products': products})

def productsWPageView(request):
    products = Product.objects.filter(gender='mujer')
    return render(request, 'core/productsW.html', {'products': products})

def searchPageView(request):
    if request.method == "POST":
        searched = request.POST.get("busqueda")
        products = Product.objects.filter(name__contains=searched)
        
        return render(request, 'core/searchproduct.html', {'products':products})
    else:
        return render(request, 'core/searchproduct.html', {})

@login_required
def editProductPageView(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('producto', pk=pk)  # Redirect to product detail view
    else:
        form = ProductForm(instance=product)
    return render(request, 'core/editProduct.html', {'form': form, 'product': product})


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('productos')
    template_name = 'core/deleteproduct.html'


@login_required
def productCreatePageView(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductForm()
    
    return render(request, 'core/addproduct.html', {'form': form})

def singlePageView(request,pk):
    product=Product.objects.get(id=pk)
    return render(request, 'core/single.html', {'product':product})


def cartResumePageView(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request, 'cart/cartR.html', {"cart_products": cart_products, "quantities":quantities, "totals":totals})

@login_required
def cartAddPageView(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity = product_quantity)
        cart_quantity = cart.__len__()
        response= JsonResponse({'qty': cart_quantity})
        messages.success(request, ("El producto se ha agregado al carro"))
        #response= JsonResponse({'Product Name': product.name})
        return response

@login_required
def cartDeletePageView(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response= JsonResponse({'product': product_id})
        return response

@login_required
def cartUpdatePageView(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, quantity= product_qty)
        response= JsonResponse({'qty': product_qty})
        return response
        #return redirect('cart/cartR.html')