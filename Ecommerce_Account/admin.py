from django.contrib import admin
from django.contrib.auth.models import User, UserManager

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email', 'last_name')
    list_filter = ('username', 'first_name', 'email', 'last_name')
    search_fields = ('username', 'first_name', 'email', 'last_name')
    ordering = ('username', 'first_name', 'email', 'last_name')