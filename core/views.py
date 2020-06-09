from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import ListView, DetailView
from django.utils import timezone

# Create your views here.
def checkout(request):
    context = {
        
    }
    return render(request, 'checkout.html', context)


def products(request):
    context = {
        'items':Item.objects.all()
    }
    return render(request, 'product.html', context)

class HomeView(ListView):
    model = Item
    template_name = "home.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.item.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.item.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.item.add(order_item)
    return redirect("core:product", slug=slug
    )





