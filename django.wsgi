#! /usr/bin/env python

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'projects.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

path = '/home/ubuntu/public/imgsearch'

if path not in sys.path:
	sys.path.append(path)