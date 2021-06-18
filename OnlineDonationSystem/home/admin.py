from django.contrib import admin
from .models import FundCollector
from  .models import Donation
# Register your models here.

admin.site.register(FundCollector)
admin.site.register(Donation)