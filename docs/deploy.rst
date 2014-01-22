Deploy
========

We deploy the project to a webfaction host using fabric.

Webfaction config
-----------------
A webapp called supervisor containing a working release of `supervisord <http://www.supervisord.org>` should be installed.

Configuration File
------------------
A file named :file:`fabsettings.py` has to be created. It is used by the :program:`fabric deployement` script. It contains the following pythonic variables:

``WF_HOST``

  A webfaction hostname (e.g. web392)

``PROJECT_NAME``

  Name of the project. This will be used to deploy two webapps:
  * ``PROJECT_NAME``: gunicorn server, serving your django project
  * ``PROJECT_NAME_static``: static files, served by the main nginx webserver.

``REPOSITORY``
  
  The git repository used to clone project.

USER            = "grfavre"
PASSWORD        = "******"
DBNAME          = "beyondthewall"
DBUSER          = "beyondthewall"
DBPASSWORD      = ""
SETTINGS_SUBDIR = "beyondthewall"
VIRTUALENVS     = "/home/grfavre/.virtualenvs"
MAILHOST        = "smtp.webfaction.com"
MAILUSER        = "grfavre"
MAILPASSWORD    = PASSWORD
MAILADDRESS     = "info@beyondthewall.ch"
DOMAIN          = 'beyondthewall.ch'
SUBDOMAINS      = ['', 'www']

