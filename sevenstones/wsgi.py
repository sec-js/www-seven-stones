from os import environ
import sys
import site
from sevenstones.settings import BASE_DIR, VENV_DIR
# Add the site-packages of the chosen virtualenv to work with

site.addsitedir(VENV_DIR + '/lib/python3.6/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR + 'sevenstones')

environ['DJANGO_SETTINGS_MODULE'] = 'sevenstones.settings'

# Activate your virtual env
#activate_env=os.path.expanduser("/home/iantibble/jango/netdelta_1116/bin/activate_this.py")
#execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()