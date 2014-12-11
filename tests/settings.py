# coding: utf-8
from __future__ import unicode_literals

import os.path
import django

INSTALLED_APPS = ['django_ses']
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = 'tests.urls'
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware')

TEST_DISCOVER_TOP_LEVEL = os.path.dirname(__file__)

if django.VERSION[:2] < (1, 6):
    TEST_RUNNER = b'discover_runner.DiscoverRunner'
