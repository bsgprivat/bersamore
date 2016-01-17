from django.contrib import admin
from models import *

class TasterAdmin(admin.ModelAdmin):
    filter_horizontal = ('friends', 'fav_beers', 'fav_breweries', 'fav_styles')


class TastingInline(admin.TabularInline):
    model = TastingBeers


class TastingAdmin(admin.ModelAdmin):
    inlines = (TastingInline,)
    filter_horizontal = ('tasters',)

admin.site.register(TastingSession, TastingAdmin)
admin.site.register(Taster, TasterAdmin)
admin.site.register(Checkin)
