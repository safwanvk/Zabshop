from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

# Create your views here.
def checkout(request):
    context = {
        
    }
    return render(request, 'checkout.html', context)


def products(request):
    context = {
        'items':Item.objects.all()
    }
    return render(request, 'products.html', context)

class HomeView(ListView):
    model = Item
    template_name = "home.html"




