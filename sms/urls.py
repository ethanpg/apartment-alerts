from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import hello

urlpatterns = patterns('',
    url(r'^hello$', hello),
)
