from django.contrib import admin
from .models import Donacion


class DonacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','amount','donor_name')
    list_filter = ('id', 'title','amount','donor_name')

    search_fields = ('title', 'amount','donor_name')

admin.site.register(Donacion, DonacionAdmin)

