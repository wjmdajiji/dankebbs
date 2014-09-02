#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
import login.views
import contact.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dankebbs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', login.views.welcome),
    url(r'^contact/$', contact.views.contact)
)
