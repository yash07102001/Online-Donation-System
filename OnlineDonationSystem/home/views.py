from django.shortcuts import render
from .models import FundCollector #import fundcollector class
# Create your views here.
def home(request):
    FC1=FundCollector() #create object of fund collector
    FC1.id=1
    FC1.name='HELPING HAND'
    FC1.amount=50000
    FC1.reason='Covid 19'

    return render(request,'home.html',{'FC1':FC1})