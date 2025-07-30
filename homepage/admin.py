from django.contrib import admin
from .models import userinfo

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','password','is_verified', 'created_at')

admin.site.register(userinfo,UserInfoAdmin)