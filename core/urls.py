from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('checkout/', views.checkout_page, name='checkout_page'),
    path('product/', views.product_page, name='product_page')

]
