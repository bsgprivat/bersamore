from tasting.api import get_systembolaget_cookies
from tasting.views import checkin_view, stats_view, checkin_overview, baseview, tastestats
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^checkin/(?P<tasting_id>\d+)/(?P<beer_i>\d+)/$', checkin_view),
    url(r'^checkin/(?P<tasting_id>\d+)/$', checkin_view),
    url(r'^(?P<tasting_id>\d+)/$', baseview),
    url(r'^(?P<tasting_id>\d+)/stats/$', tastestats),
    url(r'^$', baseview),
    url(r'^(?P<tasting_id>\d+)/wrapitup/', stats_view),
    url(r'^overview/(?P<tasting_id>\d+)/$', checkin_overview),
    url(r'^api/cook/$', get_systembolaget_cookies),
]
