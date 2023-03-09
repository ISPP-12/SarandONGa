from django.contrib import admin

# Register your models here.
from .models import Service, ServiceAmount
admin.site.register(ServiceAmount)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'date', 'attendance', 'amount', 'asem_user', 'amount')