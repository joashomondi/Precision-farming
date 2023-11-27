from .base import *
import dj_database_url

DEBUG = False 


ALLOWED_HOSTS = ["precisionfarming.onrender.com"]

# Whitenoise settings for static files in production 
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.parse(config('DATABASE_URL'))
}
