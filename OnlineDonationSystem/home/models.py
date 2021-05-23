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