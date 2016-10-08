#
# A minimal settings file that ought to work out of the box for just about
# anyone trying this project. It's deliberately missing most settings to keep
# everything simple.
#
# A real app would have a lot more settings. The only important bit as far as
# django-FAQ is concerned is to have `faq` in INSTALLED_APPS.
#

import os

PROJECT_DIR = os.path.dirname(__file__)
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.normpath(os.path.join(PROJECT_DIR, 'faq.db')),
    }
}

SITE_ID = 1
SECRET_KEY = 'c#zi(mv^n+4te_sy$hpb*zdo7#f7ccmp9ro84yz9bmmfqj9y*c'
ROOT_URLCONF = '%s.urls' % os.path.basename(PROJECT_DIR)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.normpath(os.path.join(os.path.dirname(PROJECT_DIR), 'templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'fack',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
