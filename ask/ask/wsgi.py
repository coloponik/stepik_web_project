import os

from django.core.wsgi import get_wsgi_application

# pythonpath = '/home/user1/web/ask/ask'
# bind = '0.0.0.0:8080'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ask.settings')

application = get_wsgi_application()