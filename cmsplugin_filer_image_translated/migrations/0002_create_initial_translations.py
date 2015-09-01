# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings

def create_initial_translations(apps, schema_editor):
    """
    Create initial translations for existing images
    """
    #Image = apps.get_model("filer", "Image")
    #ImageTranslation = apps.get_model("cmsplugin_filer_image_translated", "ImageTranslation")
    default_language = 'en'

    if hasattr(settings, 'LANGUAGES') and settings.LANGUAGES:
        default_language = settings.LANGUAGES[0][0]

    from cmsplugin_filer_image_translated.models import ImageTranslation
    from filer.models import Image
    for image in Image.objects.all():
        try:
            image.translation
        except AttributeError:
            ImageTranslation.objects.language(default_language).create(
                name=image.name,
                description=image.description or '',
                alt_text=image.default_alt_text or '',
                caption=image.default_caption or '',
                image=image,
            )



class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image_translated', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_translations),
    ]
