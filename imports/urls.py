__author__ = 'steffe'
from django.conf.urls import url
from views import list_imports

urlpatterns = [
    url(r'^list_imports/$', list_imports),
]
