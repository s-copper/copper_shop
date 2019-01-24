from django.contrib import admin
from .models import MyUser


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'birthday']
    list_filter = ['username', 'birthday']


admin.site.register(MyUser, UserAdmin)
