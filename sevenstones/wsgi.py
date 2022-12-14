from os import environ
import sys
import site
from sevenstones.settings import BASE_DIR, VENV_DIR
# Add the site-packages of the chosen virtualenv to work with

site.addsitedir(VENV_DIR + '/lib/python3.10/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR + 'sevenstones')

environ['DJANGO_SETTINGS_MODULE'] = 'sevenstones.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
