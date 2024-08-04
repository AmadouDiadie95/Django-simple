"""
WSGI config for simple_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_project.settings')

# The root folder of the project
# sys.path.append('/var/www/marmite-v3-api/')
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Folder venv for the site-packages
# sys.path.append('/var/www/marmite-v3-api/venv/lib/python3.10/site-packages')

app = get_wsgi_application()
