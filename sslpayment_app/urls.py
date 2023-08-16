from django.contrib import admin
from django.urls import path
from sslpayment_app import views



app_name = "sslpayment_app"

urlpatterns = [
    path('payment/', views.payment, name='payment'),
    path('status/', views.complete, name='status'),
]