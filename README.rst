=======================================
Django Trigger Happy : Service IRC
=======================================

This service provides a way to (actually) publish data on the IRC server and channel of your choice
from a service of your choice (like RSS) from Trigger Happy

for example a new RSS item is published, django-th-irc will publish them
by connecting to the server and join the expected channel

Requirements :
==============
* django_th: 0.8.3



Installation:
=============
to get the project, from your virtualenv, do :

.. code:: python

    pip install django-th-irc

then do

.. code:: python

    python manage.py syncdb

to startup the database

Parameters :
============
As usual you will setup the database parameters.

Important parts are the settings of the available services :

Settings.py
-----------

INSTALLED_APPS
~~~~~~~~~~~~~~

add the module th_irc to INSTALLED_APPS

.. code:: python

    INSTALLED_APPS = (
        'th_irc',
    )


TH_SERVICES 
~~~~~~~~~~~
TH_SERVICES is a list of the services use by Trigger Happy

.. code:: python

    TH_SERVICES = (
        'th_irc.my_irc.ServiceIrc',
    )


Setting up : Administration
---------------------------

once the module is installed, go to the admin panel and activate it.

All you can decide here is to tell if the service requires an external authentication or not.
For django-th-irc, set it to off.

Once they are activated. User can use them.


