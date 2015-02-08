from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import hello, inbound_route

urlpatterns = patterns('',
    url(r'^hello$', hello),
    url(r'^inbound$', inbound_route)
)
