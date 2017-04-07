# à la tableau de bord

[![Build Status](https://travis-ci.org/opyate/gnashboard/.svg)](https://travis-ci.org/opyate/gnashboard)

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


Dashing stuff.


## Quickstart

Run the following commands to bootstrap your environment.

    git clone https://github.com/opyate/gnashboard
    cd gnashboard
    pip install -r requirements/dev.txt
    createdb  -h localhost -p 5432 -U postgres myownlittlestorage

    export APPLICATION_SECRET='something-really-secret'
    export DATABASE_URL=postgres://postgres@localhost:5432/myownlittlestorage
    export HTTP_BASICAUTH_USERNAME=admin
    export HTTP_BASICAUTH_PASSWORD=password
    python manage.py db upgrade
    python manage.py server


A quick test:

    # create
    curl -X POST \
      --user $HTTP_BASICAUTH_USERNAME:$HTTP_BASICAUTH_PASSWORD \
      -H 'Content-Type: application/json' \
      http://localhost:5000/kv \
      -d '{"key":"this-is-the-key", "value":{"this-is":"the-value"}}'

    # read
    curl -X GET \
      --user $HTTP_BASICAUTH_USERNAME:$HTTP_BASICAUTH_PASSWORD \
      -H 'Content-Type: application/json' \
      http://localhost:5000/latest/kv/this-is-the-key


## Deployment

In your production environment, make sure the ``APPLICATION_ENV`` environment variable is set to ``"prod"``.

The app uses Basic Auth, so set `HTTP_BASICAUTH_USERNAME` and `HTTP_BASICAUTH_PASSWORD` in the environment.

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
