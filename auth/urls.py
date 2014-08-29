'''
auth.urls.py
'''

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    ###### login and registration #####
    url(r'^login$', 'auth.views.login', name='login'),
    url(r'^logout$', 'auth.views.logout', name='logout'),
    #url(r'^register$', 'accounts.views.register', name='register'),

)
