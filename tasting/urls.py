from tasting.views import checkin_view, stats_view, checkin_overview
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^checkin/', checkin_view),
    url(r'^stats/', stats_view),
    url(r'^overview/', checkin_overview),
]
