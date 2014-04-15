import django.core.handlers.wsgi
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

application = django.core.handlers.wsgi.WSGIHandler()