from django.contrib import admin
from models import *
#from tasting.admin import TastingInline


class handle_csv_admin(admin.ModelAdmin):
    pass

    def handle_csv(modeladmin, request, queryset):
        print u'hepp'
    actions = [handle_csv, ]

admin.site.register(Beer)
admin.site.register(Brewery)
admin.site.register(Country)
admin.site.register(Style)
admin.site.register(Hops)
admin.site.register(UploadedUntappdCSV, handle_csv_admin)
