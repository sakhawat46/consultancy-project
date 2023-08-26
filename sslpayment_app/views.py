from django.shortcuts import render, redirect, HttpResponseRedirect
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
from bgd_consultancy_app.models import CustomerInfo, SelectedPackage, Package
from sslpayment_app.models import Payment_info

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



    print("#########Selected Package Info Start##########")


    # package_info = SelectedPackage.objects.all().last()
    package_info = SelectedPackage.objects.filter(user = request.user).last()

    print(package_info)
    print(type(package_info.name))
    print(package_info.name)


    mydata = Package.objects.get(name=package_info.name)
    print("/////////////////")
    print(mydata)
    print(mydata.price)
    print("/////////////////")


    if package_info.name == 'Silver':
        total_pay_amount = mydata.price
        print(total_pay_amount)
    elif package_info.name == 'Gold':
        total_pay_amount = mydata.price
        print(total_pay_amount)
    elif package_info.name == 'Platinum':
        total_pay_amount = mydata.price
        print(total_pay_amount)

    print("#########Selected Package Info End##########")


    mypayment.set_product_integration(total_amount=Decimal(total_pay_amount), currency='BDT', product_category='Service', product_name='demo-product', num_of_item=1, shipping_method='YES', product_profile='None')


    current_user = request.user
    
    print("#########current_user##########")
    print(current_user)
    # customer_info = CustomerInfo.objects.all().last()
    customer_info = CustomerInfo.objects.filter(user = request.user).last()
    print(customer_info)
    print(customer_info.name)
    print(customer_info.email)
    print(customer_info.phone_number)
    print(customer_info.country)
    print(customer_info.city)
    print(customer_info.zipcode)
    print(customer_info.address)

    mypayment.set_customer_info(name=customer_info.name, email=customer_info.email, address1=customer_info.address, address2=customer_info.address, city=customer_info.city, postcode=customer_info.zipcode, country=customer_info.country, phone=customer_info.phone_number)

    mypayment.set_shipping_info(shipping_to=customer_info.address, address=customer_info.address, city=customer_info.city, postcode=customer_info.zipcode, country=customer_info.country)

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
            return HttpResponseRedirect(reverse('sslpayment_app:purchase', kwargs={'val_id':val_id, 'tran_id':tran_id, 'amount':amount},))

        if status == 'FAILED':
            messages.warning(request, f"Your Payment is Cancel. Please Try Again.")

    return render(request, 'sslpayment/complete.html', context={})


@login_required
def purchase(request, val_id, tran_id, amount):
    pay = Payment_info.objects.create()
    # customer_info = CustomerInfo.objects.all().last()
    customer_info = CustomerInfo.objects.filter(user = request.user).last()
    pay.name = customer_info.name
    pay.email = customer_info.email
    pay.phone_number = customer_info.phone_number
    pay.payment_id = tran_id
    pay.order_id = val_id
    pay.amount = amount
    pay.save()
    # return HttpResponseRedirect(reverse('bgd_consultancy_app:home'))
    return render(request, 'sslpayment/complete.html', context={})