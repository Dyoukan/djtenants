from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Sandbox

@admin.register(Sandbox)
class SandboxAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'name')

