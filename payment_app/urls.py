# from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from payment_app import views



app_name = "payment_app"

urlpatterns = [
    # path('', views.HomePageView.as_view(), name='home'),
    # path('config/', views.stripe_config),  # new
    # path('create-checkout-session/', views.create_checkout_session), # new
    # path('', views.home, name='home'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('charge/', views.charge, name='charge'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', views.ProductLandingPageView.as_view(), name='landing'),


]