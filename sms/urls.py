from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import hello, alert_applicants

urlpatterns = patterns('',
    url(r'^hello$', hello),
    url(r'^inbound$', alert_applicants)
)
