"""
WSGI config for voidpaste_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import time
import threading

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "voidpaste_system.settings")

application = get_wsgi_application()


def delete_expired_pastes():
    while True:
        call_command('delete_expired_pastes')
        time.sleep(300)  # 300 seconds = 5 minutes


thread = threading.Thread(target=delete_expired_pastes)

thread.daemon = True

thread.start()
