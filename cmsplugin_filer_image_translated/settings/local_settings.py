"""Local settings overrides"""
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cmsplugin_filer_image_translated',
        'USER': 'cmsplugin_filer_image_translated',
        'PASSWORD': 'cmsplugin_filer_image_translated',
        'HOST': 'localhost',
        'PORT': '',
    }
}

LOCAL_PG_ADMIN_ROLE = 'postgres'
LOCAL_COVERAGE_PATH = os.path.join(os.path.dirname(__file__), '../../coverage')
