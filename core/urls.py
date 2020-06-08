from django.urls import path
from .views import HomeView 
from . import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/', views.products, name='products')

]
