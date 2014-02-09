"""Models for the ``tagging_translated`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from filer.models import Image
from hvad.models import TranslatableModel, TranslatedFields


# TODO auto-create/-delete translations with images


class ImageTranslation(TranslatableModel):
    """
    Translateable fields for the ``filer.Image`` model.

    Since we can't update the `Image` model from `django-filer` directly to
    become a `TranslatableModel`, we create this translation model and attach
    it via `OneToOneField`.

    """
    image = models.OneToOneField(
        Image,
        verbose_name=_('Image'),
        related_name='translation',
    )

    translations = TranslatedFields(
        name=models.CharField(
            max_length=256,
            verbose_name=_('Name'),
            blank=True,
        ),
        description=models.TextField(
            max_length=256,
            verbose_name=_('Description'),
            blank=True,
        ),
        alt_text=models.CharField(
            max_length=512,
            verbose_name=_('Alt text'),
            blank=True,
        ),
        caption=models.CharField(
            max_length=512,
            verbose_name=_('Caption'),
            blank=True,
        ),
    )

    def __unicode__(self):
        return u'Translations for {0}'.format(self.image.original_filename)
