from tasting.views import checkin_view, stats_view
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^checkin/', checkin_view),
    url(r'^stats/', stats_view),
]
