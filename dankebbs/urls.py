#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
import login.views
import contact.views

urlpatterns = patterns('',
)

urlpatterns += patterns('',
    url(r'^$', login.views.welcome),
)

urlpatterns += patterns('',
    url(r'^contact/$', contact.views.contact),
)