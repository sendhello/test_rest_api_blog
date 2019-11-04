import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_api_blog.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
