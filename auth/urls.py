'''
auth.urls.py
'''
from django.conf.urls import patterns, url


urlpatterns = patterns('',

    ###### login and logout #####
    url(r'^login$', 'auth.views.login', name='login'),
    url(r'^logout$', 'auth.views.logout', name='logout'),

)