from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = (
        'email', 'full_name', 'employee_id', 'function',
        'service', 'is_staff', 'is_active',
    )
    list_filter = (
        'is_staff', 'is_superuser', 'is_active',
        'groups', 'service',
    )
    search_fields = (
        'email', 'first_name', 'last_name',
        'employee_id', 'function',
    )
    ordering = ('last_name', 'first_name')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Informations personnelles'), {
            'fields': ('first_name', 'last_name', 'phone_number', 'employee_id'),
        }),
        (_('Fonction'), {
            'fields': ('function', 'service'),
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Dates importantes'), {
            'fields': ('last_login', 'date_joined'),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name',
                'password1', 'password2', 'is_staff',
                'is_active', 'groups',
            ),
        }),
    )

    filter_horizontal = ('groups', 'user_permissions')
