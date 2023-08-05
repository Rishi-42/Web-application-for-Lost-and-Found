from django.contrib import admin
from .models import Accounts
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'last_login', 'date_created', 'is_active')
    list_display_links=('email', 'username')
    readonly_fields= ('date_created', 'last_login')
    ordering = ('date_created',)
    search_fields = ('email', 'username')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Accounts, AccountAdmin)