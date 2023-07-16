from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.shortcuts import render, get_object_or_404, redirect
from bgd_consultancy_app.models import CustomerInfo, CompanyInfo, Blog
from bgd_consultancy_app.forms import CustomerInfoForm, CompanyInfoForm, SelectedPlanForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages #import messages
from django.http import JsonResponse
import json
from .models import *

#Dependency Add
# from django.views.generic import ListView, CreateView, UpdateView
# from bgd_consultancy_app.models import Person, Country,City,Business,Package
# from bgd_consultancy_app.forms import PersonForm




# User Module

# from django.contrib.auth import get_user_model
# from login_app.models import User

# User = get_user_model()





# Create your views here.

def home(request):
    diction = {}
    return render(request,'bgd_consultancy_app/home.html', context = diction)




def booking(request):
    if request.user.is_authenticated:
        form1 = CustomerInfoForm()
        form2 = CompanyInfoForm()
        package_info = SelectedPlan.objects.last()
        if request.method == "POST":
            form1 = CustomerInfoForm(data=request.POST)
            form2 = CompanyInfoForm(data=request.POST)

            if form1.is_valid() and form2.is_valid():
                form1.instance.user = request.user
                form2.instance.user = request.user

                form2.instance.package_information = package_info

                form1.save()
                form2.save()
                messages.success(request, "Booking Successfully Completed.")
                return HttpResponseRedirect(reverse('payment_app:landing'))
        diction = {'form1':form1, 'form2':form2, 'package_info': package_info}
        # print("///////////////Package Info////////////////")
        # print(package_info)
        return render(request,'bgd_consultancy_app/booking.html', context = diction)
    else:
        return redirect('login_app:login')




def package(request):
    # packages = Package.objects.all().order_by('-id')
    # diction = {'packages' : packages}
    # print(packages)
    return render(request,'bgd_consultancy_app/package.html')


def how_it_work(request):
    diction = {}
    return render(request,'bgd_consultancy_app/how_it_work.html', context = diction)


def blog(request):
    all_blog = Blog.objects.all().order_by('-id')
    diction = {'all_blog': all_blog}
    return render(request,'bgd_consultancy_app/blog.html', context = diction)


def blog_details(request, slug):

    # access without loop in template
    blog = Blog.objects.get(slug=slug)

    diction = {'blog':blog}
    return render(request, 'bgd_consultancy_app/blog_details.html', context = diction)



def form_an_llc(request):
    diction = {}
    return render(request,'bgd_consultancy_app/form_an_llc.html', context = diction)

def contact_us(request):
    diction = {}
    return render(request,'bgd_consultancy_app/contact_us.html', context = diction)


def business_guide(request):
    diction = {}
    return render(request,'bgd_consultancy_app/business_guide.html', context = diction)


def business_name_generator(request):
    diction = {}
    return render(request,'bgd_consultancy_app/business_name_generator.html', context = diction)



def form_c_corporation(request):
    diction = {}
    return render(request,'bgd_consultancy_app/form_c_corporation.html', context = diction)


def form_s_corporation(request):
    diction = {}
    return render(request,'bgd_consultancy_app/form_s_corporation.html', context = diction)


def form_non_profit(request):
    diction = {}
    return render(request,'bgd_consultancy_app/form_non_profit.html', context = diction)





#Dependency Add


# class PersonCreateView(CreateView):
#     model = Person
#     form_class = PersonForm
#     template_name = 'dependency/person_form.html'
#     success_url = reverse_lazy('bgd_consultancy_app:booking')


# def load_cities(request):
#     country_id = request.GET.get('country')
#     cities = City.objects.filter(country_id=country_id).order_by('name')
#     return render(request, 'dependency/city_dropdown_list_options.html', {'cities': cities})

# def load_business(request):
#     city_id = request.GET['city']
#     business = Business.objects.filter(city_id=city_id).order_by('name')
#     return render(request, 'dependency/business_dropdown_list_options.html', {'business': business})

# def load_packages(request):
#     business_id = request.GET['business']
#     packages = Package.objects.filter(business_id=business_id).order_by('name')
#     return render(request, 'dependency/package_dropdown_list_options.html', {'packages': packages})




# New Package Add

def index(request):
    countries = Country.objects.all()
    locations = Location.objects.all()
    business_plans = BusinessPlan.objects.all()

    context = {
        'countries': countries,
        'locations': locations,
        'business_plans': business_plans,
    }

    return render(request, 'bgd_consultancy_app/index.html', context)


def get_locations(request):
    country_id = request.GET.get('country_id')
    locations = Location.objects.filter(c_name=country_id)

    html = '<option value="">Select Location</option>'
    for location in locations:
        html += f'<option value="{location.id}">{location.l_name}</option>'

    return JsonResponse({'html': html})

def get_business_plans(request):
    location_id = request.GET.get('location_id')
    business_plans = BusinessPlan.objects.filter(location=location_id)

    html = '<option value="">Select Business Plan</option>'
    for business_plan in business_plans:
        html += f'<option value="{business_plan.id}">{business_plan.name}</option>'

    return JsonResponse({'html': html})




def get_values(request):
    business_plan_id = request.GET.get('business_plan_id')
    business_plan = BusinessPlan.objects.get(id=business_plan_id)
    location = business_plan.location
    country = location.c_name

    data = {
        'value1': business_plan.value1,
        'value2': business_plan.value2,
        'value3': business_plan.value3,
    }

    selected_plan = SelectedPlan(
        country=country,
        location=location,
        business_plan=business_plan,
        value1=data['value1'],
        value2=data['value2'],
        value3=data['value3']
    )

    selected_plan.save()

    return JsonResponse(data)