from django.contrib import admin

# Register your models here.
from djongo.contrib inport admin
from .models import *

class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'notification_email')

admin.site.register(Customer, AppAdmin, Supplier, Product, Order, CostCenter)