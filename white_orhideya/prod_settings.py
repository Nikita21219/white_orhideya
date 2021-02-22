from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(11!&dhthrycbs625hj92&^he52p1_(vhw)q)nmew*32l,pr?'


DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '188.93.210.49'] 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycorg2',
        'NAME': 'banket',
        'USER': 'userdb',
        'PASSWORD': 'marader3202',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATICFILES_DIR = (
    os.path.join(BASE_DIR, "static"),
)
