from django.contrib import admin
from models import *


class TasterAdmin(admin.ModelAdmin):
    filter_horizontal = (u'friends', u'fav_beers', u'fav_breweries', u'fav_styles')
    search_fields = (u'name', )


class TastingInline(admin.TabularInline):
    model = TastingBeers


class TastingAdmin(admin.ModelAdmin):
    inlines = (TastingInline,)
    filter_horizontal = (u'tasters',)
    search_fields = (u'name', u'description')


class CheckinAdmin(admin.ModelAdmin):
    search_fields = (u'beer',)
    list_filter = (u'tasting__date', u'beer__brewery')
    list_display = (u'taster', u'beer')

admin.site.register(TastingSession, TastingAdmin)
admin.site.register(Taster, TasterAdmin)

#TODO: no need?
admin.site.register(Checkin, CheckinAdmin)
