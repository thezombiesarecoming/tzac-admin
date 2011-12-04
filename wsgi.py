import os
from os.path import join, dirname
import sys

sys.path.insert(0, join(dirname(__file__), "website"))

if "DJANGO_SETTINGS_MODULE" not in os.environ:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()