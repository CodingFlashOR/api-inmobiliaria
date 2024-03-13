"""
ASGI config for prueba project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

from django.core.asgi import get_asgi_application
from manage import set_django_settings_module


set_django_settings_module()

application = get_asgi_application()