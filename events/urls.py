from django.urls import path
from . import views
#from django import views

#calls the functions you want from views.py

urlpatterns = [
    path('', views.index,name="index"),
    #path('Shop', views.shop,name='shop'),
    path('cart', views.cart,name='cart'),
    path('checkout', views.checkout,name='checkout'),
    #path('login', views.login,name='login'),
    path('contactus', views.contactus,name='contactus'),
]
