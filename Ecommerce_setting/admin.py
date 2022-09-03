from django.contrib import admin
from .models import SiteSetting, BankAccount

# class SettingAdmin(admin.ModelAdmin):
#     list_display = ['title', 'first_email', 'first_phone']



admin.site.register([SiteSetting,BankAccount])