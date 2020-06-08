from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    context = {
        'items':Item.objects.all()
    }
    return render(request, 'home.html', context)


def checkout(request):
    context = {
        'items':Item.objects.all()
    }
    return render(request, 'checkout.html', context)


def products(request):
    context = {
        'items':Item.objects.all()
    }
    return render(request, 'products.html', context)