from cellar.views import beer_view

__author__ = 'steffe'

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^beer/', beer_view),
]
