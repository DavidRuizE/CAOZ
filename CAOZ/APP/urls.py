from django.urls import path
from APP.views import *
from . import views


urlpatterns =[
    path("", homePageView.as_view(), name= "home"),
    path("registro/", views.singupView, name= "registro"),
    path("accede/", views.loginPageView, name= "login"),
    path("logout/", views.logoutPageView, name= "logout"),
    path("productos/", views.productsPageView, name= "productos"),
    path("producto/<int:pk>", views.singlePageView, name= "producto"),
    path("carro/", views.cartResumePageView, name="carro"),
    path("carro/añadir", views.cartAddPageView, name="carro-add"),
    path("carro/eliminar", views.cartDeletePageView, name="carro_delete"),
    path("carro/actualizar", views.cartUpdatePageView, name="carro-update"),
]