# Settings that are unique to local dev go here
from .base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': 'NicolHawkins',
        'PASSWORD': 'dbpassword',
        'HOST': 'username.mysql.pythonanywhere-services.com',
    }
}

#'django.contrib.staticfiles',  this is needed to populate images on results.html
INSTALLED_APPS += ['django.contrib.staticfiles']



# Add in Debug Toolbar Middleware
# MIDDLEWARE = [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ] + MIDDLEWARE

# Required configuration for debug toolbar
INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

