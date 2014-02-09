# flake8: noqa
from cmsplugin_filer_image_translated import settings
from django.core.management import setup_environ
setup_environ(settings)

from development_fabfile.fabfile import *
from fabfile.local import *
