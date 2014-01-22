Install
=========

This is where you write how to get a new laptop to run this project.


Environment variables
---------------------

We use env vars to store critical informations. A good way of dealing with these variables::
    
    cp config/postactivate.tpl postactivate
    vi postactivate
    cat postactivate >> ~/.virtualenvs/sportfac/bin/postactivate
    source ~/.virtualenvs/sportfac/bin/postactivate

