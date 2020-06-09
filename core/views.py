from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import ListView, DetailView, View
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
    paginate_by = 10
    template_name = "home.html"

class OrderSummaryView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have active order")
            return redirect("/")
        
   



class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"
@login_required
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
            messages.info(request, "This item quantity was updated.")
        else:
            order.item.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("core:product", slug=slug)
            
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.item.add(order_item)
        messages.info(request, "This item was added to your cart.")
    return redirect("core:product", slug=slug)
@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.item.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
                )[0]
            order.item.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("core:product", slug=slug) 
    else:
        messages.info(request, "You do not have  an active order.")
        return redirect("core:product", slug=slug)
    return redirect("core:product", slug=slug)
          
    



