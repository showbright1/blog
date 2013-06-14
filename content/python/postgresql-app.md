Title: PostgreSQL app for Mac OSX
Date: 2013-06-13
Author: Michael Martinez

OSX users who develop Python applications (any application, really) that use PostgreSQL are in luck. If you are looking
for, quite possibly, the easiest way to install, run and use the most advanced open source database on the planet
(provided you are using Mac OSX > 10.7).[PostgresSQL.app](http://postgresapp.com/) | [docs](http://postgresapp.com/documentation)
- will make your life very happy. When you just want to run PostgreSQL and get to coding, Postgresgl.app from
[Matt Thompson](http://mattt.me/) and the awesome guys at [Heroku](http://postgres.heroku.com/) is where its at.

If you have ever used postgreSQL from the commandline you have undoubtedly felt this pain:

    :::bash
    pg_ctl -D /usr/local/var/postgres status
    pg_ctl -D /usr/local/var/postgres start
    pg_ctl -D /usr/local/var/postgres status
    pg_ctl -D /usr/local/var/postgres stop -s -m fast

This is just to start and/or check on the darn thing. Then you can enter the `psql` command to access the `$USER` database.
Remember that the $USER database doesn't have a password or user like it would in a production environment. The postgreSQL
app simplifies this process by allowing you to start postgreSQL like any other mac app, click on the app. Once the app
initializes, you get the cool little elephant in your toolbar.

The only thing you need to do besides installing the app is add one line to your `.bashrc` or in my case, `.zshrc`.

    :::bash
    PATH="/Applications/Postgres.app/Contents/MacOS/bin:$PATH"

With this done you can now create a database:

    :::bash
    $ psql
    psql (9.2.2)
    Type "help" for help.

    $ michaelmartinez=# CREATE DATABASE my_data;
    # If you want to delete the database you just created
    $ michaelmartinez=# DROP DATABASE my_data;

note: don't forget the semi-colon!

To use this with Django you need to install the psycopg2 package then its just a matter of adding the correct parameters
to your `DATABASE` settings:


    :::python
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "[YOUR_DATABASE_NAME]",
            "USER": "",
            "PASSWORD": "",
            "HOST": "localhost",
            "PORT": "",
        }
    }


To use this with your Flask app, you can use the Flask-SQLAlchemy extension or SQLAlchemy on its own:


    :::python
    from flask import Flask
    from flask.ext.sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/[YOUR_DATABASE_NAME]'
    db = SQLAlchemy(app)

Vanilla SQLAlchemy


    :::python
    from sqlalchemy import create_engine
    engine = create_engine('postgresql://localhost/[YOUR_DATABASE_NAME]')