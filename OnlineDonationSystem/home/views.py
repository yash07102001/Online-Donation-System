from django.shortcuts import render
from datetime import date
from .models import Donation
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
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        d=Donation()
        d.fname=fname
        d.amount=request.POST['amt']
        d.phone_no=request.POST['phone_number']
        d.date=date.today()
        d.activity=request.POST['ActivityName']
        d.paymentmethod=request.POST['paymentMethod']
        user=request.user
        d.userId=user.id
        d.save()
        d = Donation.objects.filter(userId=user.id)
        context = {
            'user': user,
            'd': d,
        }
        return render(request, 'Recent-Donations.html', context=context)
    else:
        user =request.user
        d=Donation.objects.filter(userId=user.id)
        context = {
            'user': user,
            'd':d,
        }
        return render(request, 'Recent-Donations.html', context=context)