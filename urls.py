'''
main.urls.py

'''

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

import auth, main, artists

urlpatterns = patterns('',

    ###### index #####
    url(r'^$', 'main.views.index'),

    ##### login, logout, profile #####
    url(r'^auth/', include('auth.urls', namespace='auth')),

    ##### registration #####
    url(r'^accounts/', include('registration.backends.default.urls')),
    
    ##### profile #####
    url(r'^artists/', include('artists.urls', namespace='artists')),   

    ##### admin docs #####
    #this url must be placed before /admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    ##### admin #####
    url(r'^admin/', include(admin.site.urls)),

    ##### mongonaut #####
    url(r'^mongonaut/', include('mongonaut.urls')),

)
