'''
artists/urls.py
'''
from django.conf.urls import patterns, url
from views import ArtistDetailView


urlpatterns = patterns('',

    url(r'^(?P<slug>[\w.@+-]+)/$', ArtistDetailView.as_view(), name="artist_detail"),

)