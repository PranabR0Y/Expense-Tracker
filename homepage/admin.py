from django.contrib import admin
from .models import userinfo,Services

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','password','is_verified', 'created_at')

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title','link','image')

admin.site.register(userinfo,UserInfoAdmin)
admin.site.register(Services,ServicesAdmin)