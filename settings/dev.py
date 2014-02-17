# DJANGO DEVELOPMENT SETTINGS
'''
For dev environ only, create a dummy_emails directory in the main project
directory...or use the console backend.

For staging, use Bandit to test emails. (See below.)

TODO: Fix registration e-mail templates.

'''

from .base import *

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += (
    'debug_toolbar',
    'bandit',
)


########## ADD'L DEBUG CONFIGURATION
TEMPLATE_DEBUG = DEBUG

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
}
########## END ADD'L DEBUG CONFIGURATION


########## ADD'L EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/1.4/topics/email/#file-backend
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = PROJECT_DIR.child("dummy_emails") # change this to a proper location

# For staging, see: https://django-email-bandit.readthedocs.org/en/latest/
#EMAIL_BACKEND = 'bandit.backends.smtp.HijackSMTPBackend'
#BANDIT_EMAIL = 'you@example.com'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = "localhost"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025
########## END ADD'L EMAIL CONFIGURATION