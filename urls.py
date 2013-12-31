'''
main.urls.py

TODO: Wire in django-registration
'''

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

import main
import accounts
#import registration


urlpatterns = patterns('',

    ##### login and registration #####
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    ###### index #####
    url(r'^$', 'main.views.index'),

    ##### admin #####
    url(r'^admin/', include(admin.site.urls)),

)
