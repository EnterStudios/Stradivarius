from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from accounts.forms import AuthenticationForm


def index(request):
    form = AuthenticationForm()
    return render(request, 'index.html', { 'form': form })

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')