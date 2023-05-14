# from django.conf.urls import url
from django.urls import path
from bgd_consultancy_app import views

#Dependency Add
from bgd_consultancy_app.views import *

app_name = "bgd_consultancy_app"

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.booking, name='booking'),
    path('package/', views.package, name='package'),
    path('how_it_work/', views.how_it_work, name='how_it_work'),
    path('blog/', views.blog, name='blog'),
    path('blog/<str:slug>', views.blog_details, name='blog_details'),
    path('form_an_llc/', views.form_an_llc, name='form_an_llc'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('business_guide/', views.business_guide, name='business_guide'),
    path('business_name_generator/', views.business_name_generator, name='business_name_generator'),
    # path('incorporate/', views.incorporate, name='incorporate'),
    # path('add_person', views.person, name = "person"),
    # path('cities', views.cities, name = "cities"),
    path('form_c_corporation/', views.form_c_corporation, name='form_c_corporation'),
    path('form_s_corporation/', views.form_s_corporation, name='form_s_corporation'),
    path('form_non_profit/', views.form_non_profit, name='form_non_profit'),



    #Dependency Add
    # path('dependency/', views.PersonCreateView.as_view(), name='person_add'),
    # path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    # path('ajax/load-business/', views.load_business, name='ajax_load_business'),
    # path('ajax/load-packages/', views.load_packages, name='ajax_load_packages'),



    # New Package Add

    path('package_applay', index, name='index'),
    path('get_locations/', get_locations, name='get_locations'),
    path('get_business_plans/', get_business_plans, name='get_business_plans'),
    path('get_values/', get_values, name='get_values'),



]