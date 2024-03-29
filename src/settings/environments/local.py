import os

from .base import *
from settings.constans import Environments


if config("ENVIRONMENT_STATUS") == Environments.DEVELOPMENT.value:
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []

    # Database
    # https://docs.djangoproject.com/en/4.2/ref/settings/#databases
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.2/howto/static-files/
    STATIC_URL = "static/"

    STATIC_ROOT = os.path.join("app", "static")

    STATICFILES_STORAGE = (
        "whitenoise.storage.CompressedManifestStaticFilesStorage"
    )
