from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_company', 'is_user']
    list_filter = ['is_company', 'is_user']

admin.site.register(CustomUser, CustomUserAdmin)
