#!/usr/bin/env python
from django.core.management import execute_manager
import imp
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

if "DJANGO_SETTINGS_MODULE" not in os.environ:
    os.environ["DJANGO_SETTINGS_MODULE"] = "website.settings.development"

try:
    __import__(os.environ["DJANGO_SETTINGS_MODULE"], globals(), locals())
except ImportError, e:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

settings = sys.modules[os.environ["DJANGO_SETTINGS_MODULE"]]

if __name__ == "__main__":
    execute_manager(settings)
