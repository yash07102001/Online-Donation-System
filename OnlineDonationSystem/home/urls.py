from django.urls import path
from . import views

urlpatterns = [
    # path('Home',views.home,name='home'),#temporary home, redirect after login
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('donate',views.donate,name='donate'),
    path('mydonation',views.mydonation,name='mydonation'),
    ]