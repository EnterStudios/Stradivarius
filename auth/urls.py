'''
auth.urls.py
'''

from django.conf.urls import patterns, include, url
from views import UserDetailView


urlpatterns = patterns('',

    ###### login and registration #####
    url(r'^login$', 'auth.views.login', name='login'),
    url(r'^logout$', 'auth.views.logout', name='logout'),
    #url(r'^register$', 'accounts.views.register', name='register'),

    #TODO: move this URL conf to main/ or accounts/
    ###### profile #####
    url(r'^(?P<slug>[\w.@+-]+)/$', UserDetailView.as_view(), name="user_detail"),
)