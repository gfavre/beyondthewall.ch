Deploy
========

We deploy the project to a webfaction host using fabric.

Webfaction config
-----------------
A webapp called ``supervisor`` containing a working release of `supervisord <http://www.supervisord.org>`_ has to be installed prior to deploying your project. 

Virtualenv and virtualenvwrapper have to be installed on the webfaction host.

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

``USER`` 
  
  Webfaction username (to log in and to create webapps.

``PASSWORD``  

  Webfaction password for user ``USER``

``DBNAME``  
  
  Name of the database that will be created (postgres)
  
``DBUSER``  
  
  Database user that will be created to establish the connection to the database.

``DBPASSWORD``  
  
  Password used by ``DBUSER`` to connect to ``DBNAME`` database.

``SETTINGS_SUBDIR``

  Where to find the django settings inside your ``PROJECT_NAME``

``VIRTUALENVS``  
  
  Path to your virtualenvs

``MAILHOST``  
  
  Server to be used to send mail.
  
  *Default*: ``smtp.webfaction.com``

``MAILUSER``

  User that will connect to the mail server. 
  
  *Default*: ``USER``

``MAILPASSWORD``

  Password used by ``MAILUSER`` to connect to ``MAILHOST``
  
  *Default*: ``PASSWORD``

``MAILADDRESS``

  Outgoing mail address

``DOMAIN``

  Domain that will host the project (e.g. yourdomain.com)

``SUBDOMAINS``

  Subdomains that will host the project.
  
  *Default*: ``['', 'www']``

