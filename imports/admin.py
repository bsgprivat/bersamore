from django.contrib import admin
from .models import *
# Register your models here.

class ImportBeerAdmin(admin.ModelAdmin):
    list_display = (u'name', u'sysbol_id', u'size', u'available', u'sysbol_price', u'latest_update',)
    list_filter = (u'latest_update', u'available')

admin.site.register(ImportedBeer, ImportBeerAdmin)
