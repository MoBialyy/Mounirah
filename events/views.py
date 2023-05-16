from django.shortcuts import render
from .models import Product
from .models import User

def index(request):
    return render(request,'events/index.html',{'pro':Product.objects.all()})
#def shop(request):
 #   return render(request,'events/shop.html',{})
def cart(request):
    return render(request,'events/cart.html',{})
def checkout(request):
    return render(request,'events/checkout.html',{})
#def login(request):
    #return render(request,'events/login12.html',{'user':User.objects.all()})
def contactus(request):
    return render(request,'events/contactus.html',{})


