from django.contrib import admin
from .models import Stock

class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','quantity')
    list_filter = ('id', 'name','quantity')

    search_fields = ('id', 'name','quantity')

admin.site.register(Stock, StockAdmin)