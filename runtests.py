"""
This code provides a mechanism for running django_ses' internal
test suite without having a full Django project.  It sets up the
global configuration, then dispatches out to `call_command` to
kick off the test suite.

## The Code
"""
# coding utf-8
from __future__ import unicode_literals

import os
import django
from django.core.management import call_command

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

if django.VERSION[:2] >= (1, 7):
    django.setup()

call_command("test", "tests", settings='tests.settings')
