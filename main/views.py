'''
main/views.py
'''
from django.shortcuts import render
from auth.forms import AuthenticationForm


def index(request):
    form = AuthenticationForm()
    return render(request, 'index.html', { 'form': form })
