from django.urls import path, include
from .views import *
urlpatterns = [
    path('product-list/', ProductView.as_view(), name='product-list'),
    path('order-detail/<id>', OrderDetailView.as_view() ,name='order-detail'),
    path('create-checkout-session/', create_checkout_session, name='create-checkout-session'),
]