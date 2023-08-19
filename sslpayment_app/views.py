from django.shortcuts import render, redirect
import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from bgd_consultancy_app.models import CompanyInfo
from django.views.generic import TemplateView

# Create your views here.


@login_required
def payment(request):

    # companyinfo = CompanyInfo.objects.get_or_create(user=request.user)

    # if not companyinfo[0].is_fully_filled():
    # # if not request.user.companyinfo.is_fully_filled():
    #     messages.info(request, f'Please fill up all the fields')
    #     return redirect("bgd_consultancy_app:booking")

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




@csrf_exempt
def complete(request):
    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST
        # print(payment_data)
        status = payment_data['status']

        
        if status == 'VALID':

            tran_id = payment_data['tran_id']
            val_id = payment_data['val_id']
            amount = payment_data['amount']
            bank_tran_id = payment_data['bank_tran_id']

            messages.success(request, f"Your Payment Successfully Complete.")

        if status == 'FAILED':
            messages.warning(request, f"Your Payment is Cancel. Please Try Again.")

    return render(request, 'sslpayment/complete.html', context={})