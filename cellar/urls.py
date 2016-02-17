from cellar.views import beerfinder, brewery_view, style_view, beer_view

__author__ = 'steffe'

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^beer/(?P<beer_id>\d+)/$', beer_view),
    url(r'^beerfinder/$', beerfinder),
    url(r'^brewery/(?P<brewery_id>\d+)/$', brewery_view),
    url(r'^style/(?P<style_id>\d+)/$', style_view),
]
