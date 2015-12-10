# à la tableau de bord

[![Build Status](https://travis-ci.org/opyate/application/.svg)](https://travis-ci.org/opyate/application)

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


Dashing stuff.


## Quickstart

First, set your app's secret key as an environment variable. For example, example add the following to ```.bashrc``` or ```.bash_profile```.

    export APPLICATION_SECRET='something-really-secret'


Then run the following commands to bootstrap your environment.

    git clone https://github.com/opyate/application
    cd application
    pip install -r requirements/dev.txt
    python manage.py server

Once you have installed your DBMS, run the following to create your app's database tables and perform the initial migration:

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py server

And finally, here's the backend developer's version of a pretty welcome screen:

    # create a foo
    curl -X POST \
    -H 'Content-Type: application/json' \
    http://localhost:3000/foo \
    -d '{"bar":42}'
    # read it back
    curl -X GET \
    -H 'Accept: application/json' \
    http://localhost:3000/foo


## Deployment

In your production environment, make sure the ``APPLICATION_ENV`` environment variable is set to ``"prod"``.

## Shell

To open the interactive shell, run

    python manage.py shell

By default, you will have access to ``app``, ``db``, and the ``Foo`` model.

## Running Tests

To run all tests, run

    python manage.py test


## Migrations

Whenever a database migration needs to be made. Run the following commmands:

    python manage.py db migrate

This will generate a new migration script. Then run:

    python manage.py db upgrade

To apply the migration.

For a full migration command reference, run ``python manage.py db --help``.

# API

Assuming a server running on [localhost:5000](http://localhost:5000):

## [/](http://localhost:5000/)

Root. Nothing here.

## [/kv](http://localhost:5000/kv)

Key-value store.
Supports `GET`, `POST`, `PUT`, `DELETE`.

## [/latest/kv](http://localhost:5000/latest/kv)

Read-only alternative API for Key-value store.

## [/latest/kv/{key}](http://localhost:5000/latest/kv/{key})

Same as above, by `key`.

## [/page](http://localhost:5000/page)

Page store.
Supports `GET`, `POST`, `PUT`, `DELETE`.

## [/latest/page](http://localhost:5000/latest/page)

Read-only alternative API for Page store.

## [/latest/page/{name}](http://localhost:5000/latest/page/{name})

Same as above, by `name`.

Or, post an HTML file to a named endpoint:

    curl http://localhost:5000/latest/page/foo -F html=@yourfile.html
