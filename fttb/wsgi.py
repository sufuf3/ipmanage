# coding=UTF-8
"""
WSGI config for fttb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fttb.settings")

from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()

#from dj_static import Cling
#application = Cling(get_wsgi_application())



import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    content = "您訪問的網站不存在"
    remote_addr = environ.get('REMOTE_ADDR')
    if remote_addr and not remote_addr.startswith('140.113.'):
        start_response('600 domain_not_exists', [('Content-Type', 'text/html; charset=utf-8'),])
        return [content]
    return _application(environ, start_response)


from dj_static import Cling
application = Cling(get_wsgi_application())

