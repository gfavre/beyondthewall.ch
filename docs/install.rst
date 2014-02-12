Install
=========


Environment variables
---------------------

We use env vars to store critical informations. A good way of dealing with these variables::
    
    cp config/postactivate.tpl postactivate
    vi postactivate
    cat postactivate >> ~/.virtualenvs/beyondthewall/bin/postactivate
    source ~/.virtualenvs/beyondthewall/bin/postactivate

