Welcome to Version Check's documentation!
=========================================

**Note**: this does not completed yet. It should work.

Overview
--------

Provides responses to queries about add-ons, by telling you which one needs to
be updated.

Installing
----------

This service needs to point to a zamboni database. Contained in there will be
the addons, versions and files that this service examines. Copy over the
settings file and alter it appropriately::

        cp settings-local.py.dist settings-local.py

Running service with gunicorn
-----------------------------
To run the scripts you’ll want a wsgi server, on prod this is likely nginx and
gunicorn and. Locally you can optionally use gunicorn, for example::

        pip install gunicorn

Then you can do::

        ./serve

Testing
-------

Tests are currently run from zamboni which import this from PyPi. Hopefully
we'll figure out a nice solution to port them all over here soon. In your nice
friendly zamboni install run the following::

        python manage.py test apps/addons/tests/test_update.py

Until we flip to using this as the main version check source, to get these
tests to work you'll need the `versioncheck branch`_.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _`versioncheck branch`: https://github.com/andymckay/zamboni/tree/versioncheck

