from django.db import models

# Create your models here.

#classes
class FundCollector(models.Model):
    name =models.CharField(max_length=20)
    reason=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    img =models.ImageField(upload_to='img')
    amount =models.IntegerField()

# class SucessStoties(models.Model):
#     title = models.CharField(max_length=50)
#     story= models.CharField(max_length=500)
#     img= models.ImageField(upload_to='img')

class Donation(models.Model):
    fname=models.CharField(max_length=20)
    activity=models.CharField(max_length=20)
    paymentmethod=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=15)
    address=models.CharField(max_length=50)
    amount=models.IntegerField()
    date=models.DateField()
    userId=models.IntegerField()

    def __self__(self):
        return self.id

# class TotalDonation(models.Model):
#     pass

