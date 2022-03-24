from django.contrib import admin
from django.db import OperationalError
from .models import Account, BaseUserManager
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AccountAdmin(UserAdmin):
    try:
        list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')

        readonly_fields = ('last_login', 'date_joined')

        ordering = ('date_joined',)

        list_display_links = ('email', 'first_name', 'last_name')

        filter_horizontal = ()
        list_filter = ()
        fieldsets = ()
    except OperationalError:
        pass

admin.site.register(Account, AccountAdmin)