from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','surname','email', 'sex', 'resident_place', 'address', 'telephone', 'postal_code')
    list_filter = ('id', 'name','surname','email', 'sex')

    search_fields = ('id', 'name','surname','email', 'sex', 'resident_place', 'telephone', 'postal_code')

admin.site.register(Person)