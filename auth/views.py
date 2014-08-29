'''
auth.views.py
'''
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from forms import AuthenticationForm


def login(request):
    """
    Login view
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/')
        else:
            return redirect('/')
            #: if form is invalid, would rather flash an error message on login page...
            #message = request.session['message'] = 'Hello view2!'
            #return render_to_response('accounts/login.html', {
            #'form': form,
            #'message': message,
            #}, context_instance=RequestContext(request))
    else:
        form = AuthenticationForm()

    return render_to_response('auth/login.html', {
        'form': form,
    }, context_instance=RequestContext(request))


def logout(request):
    """
    Log out view
    """
    django_logout(request)
    return redirect('/')


'''
def register(request):
    """
    User registration view.
    """
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
    return render_to_response('registration/registration_form.html', {
        'form': form,
    }, context_instance=RequestContext(request))

'''


