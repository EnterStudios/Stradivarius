'''
artists/views.py
'''
from django.views.generic.detail import DetailView
from auth.models import MyUser
from braces.views import LoginRequiredMixin


class ArtistDetailView(LoginRequiredMixin, DetailView):
    model = MyUser
    template_name = "artists/artist_detail.html"
    #use email instead of pk or username
    slug_field = "email"
    #override the context user object to profile
    context_object_name = "artist_detail"