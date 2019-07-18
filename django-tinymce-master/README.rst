django-tinymce
==============

**django-tinymce** is a Django application that contains a widget to render a form field as a TinyMCE editor.

.. image:: https://img.shields.io/pypi/v/django-tinymce.svg
        :target: https://pypi.python.org/pypi/django-tinymce

.. image:: https://img.shields.io/pypi/pyversions/django-tinymce.svg
        :target: https://pypi.python.org/pypi/django-tinymce

.. image:: https://img.shields.io/pypi/dm/django-tinymce.svg
        :target: https://pypi.python.org/pypi/django-tinymce

.. image:: https://travis-ci.org/aljosa/django-tinymce.svg?branch=master
        :target: https://travis-ci.org/aljosa/django-tinymce

.. image:: https://coveralls.io/repos/github/aljosa/django-tinymce/badge.svg?branch=master
        :target: https://coveralls.io/github/aljosa/django-tinymce?branch=master

Quickstart
==========

Install django-tinymce:

.. code-block::

    $ pip install django-tinymce

Add tinymce to INSTALLED_APPS in settings.py for your project:

.. code-block::

    INSTALLED_APPS = (
        ...
        'tinymce',
    )

Add tinymce.urls to urls.py for your project:

.. code-block::

    urlpatterns = [
        ...
        url(r'^tinymce/', include('tinymce.urls')),
    ]

In your code:

.. code-block::

    from django.db import models
    from tinymce.models import HTMLField

    class MyModel(models.Model):
        ...
        content = HTMLField()

**django-tinymce** uses staticfiles so everything should work as expected, different use cases (like using widget instead of HTMLField) and other stuff is available in documentation.

Releases
===================

Latest release is 2.6.0. It supports python 2.7, 3.4, 3.5 and Django >= 1.7.
Previous releases can be found on github, but they are no longer maintained.

Documentation
=============

http://django-tinymce.readthedocs.org/

Support and updates
===================

Use github issues https://github.com/aljosa/django-tinymce/issues

License
=======

Originally written by Joost Cassee.

This program is licensed under the MIT License (see LICENSE.txt)
