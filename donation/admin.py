from django.contrib import admin
from .models import Donation


class DonationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'amount', 'donor_name')
    list_filter = ('id', 'title', 'amount', 'donor_name')

    search_fields = ('title', 'amount', 'donor_name')


admin.site.register(Donation, DonationAdmin)
