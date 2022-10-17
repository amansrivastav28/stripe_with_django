from .models import Product, OrderDetail
from django.http.response import HttpResponseNotFound, JsonResponse
import stripe
import json
from django.conf import settings
from django.views.generic import ListView, DetailView
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
# Create your views here.

class ProductView(ListView):
    model = Product
    template_name = "stripepayment/product_list.html"
    context_object_name = 'product'


class OrderDetailView(DetailView):
    model = Product
    template_name = 'stripepayment/checkout.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = 'http://localhost:8000'
@csrf_exempt
def create_checkout_session(request):
    #request_data = json.loads(request.body)
    product = get_object_or_404(Product, pk=9)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.PaymentIntent.create(
                          amount=int(product.price * 100),
                          currency="inr",
                          automatic_payment_methods={"enabled": False},
                                        )
    # OrderDetail.product = product.id
    # OrderDetail.amount = product.price
    # OrderDetail.has_paid = 'True'
    # OrderDetail.save()
    # print(OrderDetail.objects.get(id=product.id))

    print(session)
    return JsonResponse(session)

