from django.contrib import admin
from models import *


class TasterAdmin(admin.ModelAdmin):
    filter_horizontal = (u'friends', u'fav_beers', u'fav_breweries', u'fav_styles')
    search_fields = (u'name', )
    list_display = (u'user', u'untappd_id')#, u'allow_contacts')



class TastingInline(admin.TabularInline):
    model = TastingBeers
    raw_id_fields = (u'beer',)
    ordering = (u'position', )


class TastingInviteInline(admin.TabularInline):
    model = TastingInvitation
    raw_id_fields = (u'taster',)


class TastingInviteAdmin(admin.ModelAdmin):
    def send_invite(self):
        print self

    actions = [send_invite, ]


class TastingAdmin(admin.ModelAdmin):
    inlines = (TastingInviteInline, TastingInline)
    filter_horizontal = (u'tasters',)
    search_fields = (u'name', u'description')


class CheckinAdmin(admin.ModelAdmin):
    search_fields = (u'beer',)
    list_filter = (u'tasting', u'tasting__date', u'beer__brewery')
    list_display = (u'taster', u'beer', u'date', u'tasting')


class LoginAdmin(admin.ModelAdmin):
    list_display = (u'usr', u'dt')
    list_filter = (u'usr', u'dt')
    search_fields = (u'usr__username',)


admin.site.register(TastingSession, TastingAdmin)
admin.site.register(Taster, TasterAdmin)
admin.site.register(Login, LoginAdmin)

#TODO: no need?
admin.site.register(Checkin, CheckinAdmin)
