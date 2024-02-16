from .common import *




DEBUG = True

SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'storefront3', 
        'USER': 'postgres',
        'PASSWORD': 'chlorine',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}