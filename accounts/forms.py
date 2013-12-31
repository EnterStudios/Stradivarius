'''
accounts.forms.py

TODO: AuthenticationForm needs placekeepers.
'''

from django import forms
from models import User


class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    email = forms.EmailField(widget=forms.TextInput,
                                label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label="Password (again)")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def clean(self):
        """
        Verifies that the values entered into the password fields match.

        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class AuthenticationForm(forms.Form):
    """
    Login form.
    """
    email = forms.EmailField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ['email', 'password']


'''
class PrettyAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(PrettyAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = u'username'
        self.fields['password'].widget.attrs['placeholder'] = u'password'
'''
