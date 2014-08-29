'''
artists.urls.py
'''

from django.conf.urls import patterns, include, url
from views import UserDetailView

urlpatterns = patterns('',

    ###### profile #####
    url(r'^(?P<slug>[\w.@+-]+)/$', UserDetailView.as_view(), name="user_detail"),

)
