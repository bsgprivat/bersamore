from django.contrib import admin
from models import *
#from tasting.admin import TastingInline


class handle_csv_admin(admin.ModelAdmin):
    pass

    def handle_csv(modeladmin, request, queryset):
        print u'hepp'
    actions = [handle_csv, ]


class BeerAdmin(admin.ModelAdmin):
    search_fields = (u'name', u'brewery__name', u'style__name')
    list_display = (u'name', u'brewery', u'style')
    filter_horizontal = (u'collabs', u'hops')
    list_filter = (u'brewery__country', u'brewery', u'abv', u'ibu')


class BreweryAdmin(admin.ModelAdmin):
    search_fields = (u'name', u'country__name', u'style__name')
    list_display = (u'name', u'country')
    list_filter = (u'country__name',)


class StyleAdmin(admin.ModelAdmin):
    search_fields = (u'name',)
    list_display = (u'name',)


class ForeginIDInline(admin.TabularInline):
    model = ForeignID
    raw_id_fields = (u'beer',)


admin.site.register(Beer, BeerAdmin)
admin.site.register(Brewery, BreweryAdmin)
admin.site.register(Country)
admin.site.register(Style)
admin.site.register(Hops)
admin.site.register(UploadedUntappdCSV, handle_csv_admin)
