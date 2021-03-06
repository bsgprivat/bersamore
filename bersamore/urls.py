"""bersamore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings as sett
from bersamore.views import search, index, logout_usr, user_browse, beer_browse
from tasting.api import untappd_callback
from tasting.views import (profile, settings, checkins, checkin_view,)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cellar/', include('cellar.urls')),
    url(r'^tasting/', include('tasting.urls')),
    url(r'^imports/', include('imports.urls')),
    url(r'^$', index),
    url(r'^logout/$', logout_usr),
    #url(r'^profile/$', profile),
    url(r'^checkins/$', checkins),
    url(r'^settings/$', settings),
    url(r'^checkin/(?P<beer_id>\d+)/$', checkin_view),

    url(r'^api/callback/$', untappd_callback),
    url(r'^users/$', user_browse),
    url(r'^beers/$', beer_browse),
    url(r'^profile/$', profile),
    url(r'^search/$', search),
]