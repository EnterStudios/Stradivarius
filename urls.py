'''
main.urls.py

TODO:
- wire in django-registration
- rename accounts.views, accounts.urls and templates.accounts as
  auth.views, auth.urls, and templates.auth

'''

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

import main
import accounts
#import registration


urlpatterns = patterns('',

    ##### login, logout, profile #####
    url(r'^auth/', include('accounts.urls', namespace='auth')),

    ##### registration #####
    url(r'^accounts/', include('registration.backends.default.urls')),

    ###### index #####
    url(r'^$', 'main.views.index'),

    ##### admin docs #####
    #this url must be placed before /admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    ##### admin #####
    url(r'^admin/', include(admin.site.urls)),

)
