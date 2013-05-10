Title: Basic Alembic Migrations with Flask
Date: 2013-05-10
Author: Michael Martinez

This post will cover the minimal set-up to get basic (auto-generating) Alembic migrations working within a Flask application. The pre-requisites are;
Flask, SQLAlchemy, Flask-SQLAlchemy and Alembic in case that wasn't obvious.

My current project is being built with [Flask](http://flask.pocoo.org/) utilizing [SQLalchemy](http://www.sqlalchemy.org/) as an abstraction to
my data persistence layer AKA ORM. I am also using the [Flask-SQLALchemy](http://pythonhosted.org/Flask-SQLAlchemy/)
extension to make life even easier. In the fantastic [Flask Mega Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world),
Miguel Grinburg uses [sqlalchemy-migrate](http://code.google.com/p/sqlalchemy-migrate) to manage the migrations of his database.
I found the code to be a bit heavy-handed and fragile, not to mention that sqlalchemy-migrate is incompatible with versions
of SQLAlchemy greater than 0.8, nor has it seen an update in sometime. The constant churn of packages and frameworks is a
<s>risk</s>feature of Open Source Software. One has to be comfortable with this situation and I am!

That said, to the database migration rescue comes [Alembic](http://alembic.readthedocs.org/en/latest/). This package is
written by [Mike Mayer](http://techspot.zzzeek.org/) who happens to be the father of SQLAlchemy itself. I can't
think of another person who would be more qualified to write such a tool than he. We are a truly lucky lot in this case!

On with it now!

### Get started

This first thing you need to do is create the migration environment. I suggest creating a virtualenv for your project before
you start.

Once you have activated your virutalenv:

    :::bash
    $ cd yourproject
    $ pip install alembic
    $ alembic init alembic


This command creates an Alembic directory and alembic.ini file in your project directory. Running `alembic init alembic`
creates a generic configuration. Run it as described above unless you have a multi-database or a pylons project. The docs
for this are [here.](https://alembic.readthedocs.org/en/latest/tutorial.html#creating-an-environment)

### alembic.ini

Just like SQLAlchemy, I believe Alembic is customizable to its very core, but I am no expert. For my simple mission to get Alembic running,
I chose to leave this file as is. I will revisit this aspect if conditions warrant in a future post.

### env.py

This is where I made some modifications to the generated file to get it working with Flask.

    :::python
    from __future__ import with_statement
    import os, sys
    sys.path.append(os.getcwd())
    from alembic import context
    from sqlalchemy import engine_from_config, pool
    from logging.config import fileConfig

    from <application> import app
    from <application>.models import db

    # This is the 'Generic' alembic modified with some settings
    # specific to this app

    # this is the Alembic Config object, which provides
    # access to the values within the .ini file in use.
    config = context.config

    # Overwrite the sqlalchemy.url in the alembic.ini file.
    config.set_main_option('sqlalchemy.url', app.config['SQLALCHEMY_DATABASE_URI'])

    # Interpret the config file for Python logging.
    # This line sets up loggers basically.
    fileConfig(config.config_file_name)

    # add your model's MetaData object here
    # for 'autogenerate' support
    # from myapp import mymodel
    # target_metadata = mymodel.Base.metadata
    target_metadata = db.metadata


* Import os and sys to modify the path. I am not sure if this is a bug in Alembic, but I could not get
Alembic to find my modules without appending the current working directory to my path.
* Import your app and db. Note: this is application specific as Flask will let you set these up in a few different places.
* Override the sqlalchemy.url in Alembic.ini file with a pointer to your applications database config
* Use db.metadata to provide automatic migration generation support.

### Autogenerate Migrations

    :::bash
    $ alembic revision --autogenerate -m "<insert message here>"


You can inspect and modify the migration created by looking in the `application/alembic/versions/` directory

Docs for this are [here](https://alembic.readthedocs.org/en/latest/tutorial.html#auto-generating-migrations)

### Run Migrations

    :::bash
    $ alembic upgrade head


Docs for this are [here.](https://alembic.readthedocs.org/en/latest/tutorial.html#running-our-first-migration)

... and we are good to go! Basic Alembic migrations should be running with most Flask apps.
[Flask](http://flask.pocoo.org/) is great framework for building python web apps. I plan on using it
extensively for the next few projects floating around in my head. There will be a lot more on that front
in due time. I will be sure to post more on my adventures with Flask, SQLAlchemy, Alembic and others as time permits...

