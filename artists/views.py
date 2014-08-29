'''
artists.views.py
'''

#from django.http import HttpResponseRedirect, HttpResponse
#from django.shortcuts import render_to_response, redirect
#from django.template import RequestContext
from django.views.generic.detail import DetailView
from braces.views import LoginRequiredMixin
from auth.models import MyUser

class UserDetailView(LoginRequiredMixin, DetailView):
    model = MyUser
    template_name = "artists/user_detail.html"
    #use email instead of pk or username
    slug_field = "email"
    #override the context user object to profile
    context_object_name = "user_detail"
