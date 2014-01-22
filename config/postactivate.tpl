export PYTHONPATH=%(project_dir)s/%(project)s
export PYTHONHASHSEED=random
export DJANGO_SETTINGS_MODULE="%(project)s.settings.%(settings)s"
export DB_USER="%(dbuser)s"
export DB_PASSWORD="%(dbpassword)s"
export DB_NAME="%(dbname)s"
export SECRET_KEY="%(secretkey)s"
export EMAIL_HOST="%(mailhost)s"
export EMAIL_HOST_USER="%(mailuser)s"
export EMAIL_HOST_PASSWORD="%(mailpassword)s"
export DEFAULT_FROM_EMAIL="%(mailaddress)s"
export SERVER_EMAIL="%(mailaddress)s"
export ALLOWED_HOSTS="%(allowed_hosts_str)s"
export STATIC_ROOT="%(static_root)s"
export MEDIA_ROOT="%(media_root)s"