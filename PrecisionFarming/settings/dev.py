from .base import * 
import os 

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads/")


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}