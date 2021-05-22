from django.urls import path
from . import views

urlpatterns = [
    # path('Home',views.home,name='home'),#temporary home, redirect after login
    path('',views.home,name='home'),
    ]