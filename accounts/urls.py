'''
accounts.urls.py
'''

from django.conf.urls import patterns, include, url
from views import UserDetailView


urlpatterns = patterns('',

    ###### login and registration #####
    url(r'^login$', 'accounts.views.login', name='login'),
    url(r'^register$', 'accounts.views.register', name='register'),
    url(r'^logout$', 'accounts.views.logout', name='logout'),

    ###### profile #####
    url(r'^(?P<slug>[\w.@+-]+)/$', UserDetailView.as_view(), name="user_detail"),
)