# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.OneToOneField(related_name='translation', verbose_name='Image', to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageTranslationTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='Name', blank=True)),
                ('description', models.TextField(max_length=256, verbose_name='Description', blank=True)),
                ('alt_text', models.CharField(max_length=512, verbose_name='Alt text', blank=True)),
                ('caption', models.CharField(max_length=512, verbose_name='Caption', blank=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='cmsplugin_filer_image_translated.ImageTranslation', null=True)),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'cmsplugin_filer_image_translated_imagetranslation_translation',
                'db_tablespace': '',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='imagetranslationtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
