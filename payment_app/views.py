from django.shortcuts import render, redirect
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
# from .models import Price
from django.views.generic import TemplateView
from .models import Product
from bgd_consultancy_app.models import BusinessPlan

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = Product.objects.get(id=product_id)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/payment/success/',
            cancel_url=YOUR_DOMAIN + '/payment/cancel/',
        )

        return JsonResponse({
            'id': checkout_session.id
        })
    



class SuccessView(TemplateView):
    template_name = "payment/success.html"

class CancelView(TemplateView):
    template_name = "payment/cancel.html"


class ProductLandingPageView(TemplateView):
    template_name = "payment/landing.html"

    def get_context_data(self, **kwargs):
        product = Product.objects.get(name="Test Product")
        # prices = Price.objects.filter(product=product)
        # product_demo = BusinessPlan.objects.get(value1=500)
        print("#############")
        # print(product_demo)
        print("##############")
        context = super(ProductLandingPageView,
                        self).get_context_data(**kwargs)
        context.update({
            "product": product,
            # "product_demo": product_demo,
            # "prices": prices
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context