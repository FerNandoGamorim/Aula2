"""
WSGI config for Config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import  sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Aula2.settings')

application = get_wsgi_application()

# +++++++++++ DJANGO +++++++++++ 
# Para usar seu próprio aplicativo Django, use um código como este: 
# supondo que seu arquivo de configurações do Django esteja em '/home/myusername/mysite/mysite/settings.py' 
path  =  'home/fergamorim/Aula2' 
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Aula2.settings'

## Uncomment the lines below depending on your Django version
###### then, for Django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
###### or, for older Django <=1.4
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()