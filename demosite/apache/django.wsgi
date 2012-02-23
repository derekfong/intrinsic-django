#!/usr/bin/env python
import os, sys

# make sure app's modules can be found
sys.path.append('/var/www/intrinsic-django')
sys.path.append('/var/www/intrinsic-django/demosite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'demosite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
