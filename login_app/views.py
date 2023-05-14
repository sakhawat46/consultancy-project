from multiprocessing import context
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from login_app.forms import ProfileForm, RegistrationForm
from bgd_consultancy_app.models import CompanyInfo

# Authentication function
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

# from order_app.models import Cart, Order
# from login_app.models import CustomerInfo
# from payment_app.forms import BillingAddressForm
from login_app.models import Profile

from django.views.generic import TemplateView

#messages
from django.contrib import messages

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return HttpResponse('You are authenticate')
    else:
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Create Successfully!")
                return HttpResponseRedirect(reverse('login_app:login'))
    context = {'form': form}
    return render(request, 'login_app/register.html', context)


def customerlogin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Successfully!")
                return HttpResponseRedirect(reverse('bgd_consultancy_app:home'))
    context = {
        'form': form
    }
    return render(request, 'login_app/login.html', context)



@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, "Logged Out Successfully!")
    return HttpResponseRedirect(reverse('bgd_consultancy_app:home'))


'''
class ProfileView(TemplateView):
    def get(self, request, *args, **kwargs):
        # orders = Order.objects.filter(user=request.user, ordered = True)

        # billingaddress = BillingAddress.objects.get(user=request.user)

        # billingaddress_form = BillingAddressForm(instance=billingaddress)

        profile_obj = Profile.objects.get(user=request.user)
        profileForm = ProfileForm(instance=profile_obj)
        context = {
            # 'orders' : orders,
            # 'billingaddress' : billingaddress_form,
            'profileForm' : profileForm,
        }
        
        return render(request, 'login_app/profile.html', context)


    # def post(self, request, *args, **kwargs):
    #     if request.method == 'post' or request.method == 'POST':
    #         billingaddress = BillingAddress.objects.get(user=request.user)
    #         billingaddress_form = BillingAddressForm(request.POST, instance=billingaddress)

    #         profile_obj = Profile.objects.get(user=request.user)
    #         profileForm = ProfileForm(request.POST, instance=profile_obj)
    #         if billingaddress_form.is_valid() or profileForm.is_valid():
    #             billingaddress_form.save()
    #             profileForm.save()
    #             return redirect('fashion_app:profile')
'''


def profile(request):
    # all_service = CompanyInfo.objects.all().order_by('-id')
    all_service = CompanyInfo.objects.filter(user = request.user)
    print("#################")
    print(all_service)
    print("#################")
    diction = {'all_service': all_service}
    return render(request,'login_app/profile.html', context = diction)