import os
from os.path import join, dirname
import sys

sys.path.insert(0, join(dirname(__file__), "website"))

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings.development'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()