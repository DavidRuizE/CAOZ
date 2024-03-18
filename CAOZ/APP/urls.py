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
]