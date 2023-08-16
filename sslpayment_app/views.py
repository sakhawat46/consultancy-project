from django.shortcuts import render, redirect
import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.


@login_required
def payment(request):

    store_id = 'bgd64dca86ccb86b'
    sslc_store_passcode = 'bgd64dca86ccb86b@ssl'

    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=sslc_store_passcode)

    status_url = request.build_absolute_uri(reverse('sslpayment_app:status'))

    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)

    mypayment.set_product_integration(total_amount=Decimal('20.20'), currency='BDT', product_category='Service', product_name='demo-product', num_of_item=1, shipping_method='YES', product_profile='None')

    mypayment.set_customer_info(name='John Doe', email='johndoe@email.com', address1='demo address', address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh', phone='01711111111')

    mypayment.set_shipping_info(shipping_to='demo customer', address='demo address', city='Dhaka', postcode='1209', country='Bangladesh')

    response_data = mypayment.init_payment()

    # print(response_data)

    # return render(request, 'sslpayment/payment.html', context={})
    return redirect(response_data['GatewayPageURL'])




@login_required
def complete(request):
    return render(request, 'sslpayment/complete.html', context={})