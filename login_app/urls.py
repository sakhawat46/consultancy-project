# from django.conf.urls import url
from django.urls import path
from login_app import views

app_name = "login_app"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.customerlogin, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),

]