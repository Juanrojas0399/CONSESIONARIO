"""
WSGI config for SOVERING_KING_MOTORSPORTS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

#import os

#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SOVERING_KING_MOTORSPORTS.settings')

#application = get_wsgi_application()


import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sovereing-king-motorsports.settings")
application = get_wsgi_application()
app = application
