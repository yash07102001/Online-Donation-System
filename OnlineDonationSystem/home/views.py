from django.shortcuts import render
from .models import FundCollector #import fundcollector class
# Create your views here.
def home(request):

    FC = FundCollector.objects.all()
    # FC1=FundCollector() #create object of fund collector
    # FC1.id=1
    # FC1.name='HELPING HAND'
    # FC1.amount=50000
    # FC1.reason='Covid 19'

    return render(request, 'index.html', {'FC': FC})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def donate(request):
    return render(request,'donate.html')

def mydonation(request):
    pass    #return render(request,'mydonation.html')