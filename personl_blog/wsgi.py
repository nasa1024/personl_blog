"""
WSGI config for personl_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

import sys

from django.core.wsgi import get_wsgi_application

from os.path import join, dirname, abspath


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personl_blog.settings")

application = get_wsgi_application()


PROJECT_DIR = dirname(dirname(abspath(__file__)))  # 3

sys.path.insert(0, PROJECT_DIR)  # 5

os.environ["DJANGO_SETTINGS_MODULE"] = "blog.settings"  # 7

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
