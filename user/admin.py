from django.contrib import admin
from user import models
# Register your models here.


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "rapid_api_key", "is_staff", "is_superuser", "is_active")
