from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'phone_number', 'name', 'age', 'is_staff', 'status')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'phone_number', 'name', 'age', 'image')}),
        ('Permissions',
         {'fields': (
             'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'status')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined', 'membership_validity_date')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'phone_number', 'name', 'age', 'image', 'password1',
                'password2'),
        }),
    )
    search_fields = ('username', 'email', 'phone_number', 'name')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
