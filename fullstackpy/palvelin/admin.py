from django.contrib import admin
from .models import Currency

class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate')

admin.site.register(Currency, AppAdmin)