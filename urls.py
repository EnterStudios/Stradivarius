'''
main.urls.py

'''

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

import main
import auth

urlpatterns = patterns('',

    ###### index #####
    url(r'^$', 'main.views.index'),

    ##### login, logout, profile #####
    url(r'^auth/', include('auth.urls', namespace='auth')),

    ##### registration #####
    url(r'^accounts/', include('registration.backends.default.urls')),

    ##### admin docs #####
    #this url must be placed before /admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    ##### admin #####
    url(r'^admin/', include(admin.site.urls)),

)
