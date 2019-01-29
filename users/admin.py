from django.contrib import admin
from .models import MyUser, UserAddress


class UserAddressInline(admin.TabularInline):
    model = UserAddress


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'birthday', 'email']
    list_filter = ['username', 'birthday']
    inlines = [
        UserAddressInline,
    ]




admin.site.register(MyUser, UserAdmin)
