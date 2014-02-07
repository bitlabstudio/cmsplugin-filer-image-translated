Cmsplugin Filer Image Translated
================================

Adds simple-translation to the ``Image`` admin of ``django-filer``.

Installation
------------

Prerequisites:

* Django
* django-filer
* simple-translation
* TODO: Is that all?

If you want to install the latest stable release from PyPi::

    $ pip install cmsplugin-filer-image-translated

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/cmsplugin-filer-image-translated.git#egg=cmsplugin_filer_image_translated

Add ``cmsplugin_filer_image_translated`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'cmsplugin_filer_image_translated',
    )

Run the South migrations::

    ./manage.py migrate cmsplugin_filer_image_translated


Usage
-----

TODO: Describe usage


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
