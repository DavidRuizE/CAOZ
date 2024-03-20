from django.urls import path
from APP.views import *
from . import views


urlpatterns =[
    path("", homePageView.as_view(), name= "home"),
    path("registro/", views.singupView, name= "registro"),
    path("accede/", views.loginPageView, name= "login"),
    path("logout/", views.logoutPageView, name= "logout"),
    path("productos/", views.productsPageView, name= "productos"),
    path("productos-hombre/", views.productsMPageView, name= "productosH"),
    path("productos-mujer/", views.productsWPageView, name= "productosM"),
    path("producto/<int:pk>", views.singlePageView, name= "producto"),
    path("carro/", views.cartResumePageView, name="carro"),
    path("carro/anadir", views.cartAddPageView, name="carro-add"),
    path("carro/eliminar", views.cartDeletePageView, name="carro_delete"),
    path("carro/actualizar", views.cartUpdatePageView, name="carro-update"),
    path("producto/anadir", views.productCreatePageView, name="addform"),
    path('producto/<int:pk>/editar/', views.editProductPageView, name='editar-producto'),
    path('producto/<int:pk>/delete/', ProductDeleteView.as_view(), name='eliminar-producto'),
    path("busqueda-producto/", views.searchPageView, name="busqueda-producto"),
]