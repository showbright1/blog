Title: PostgreSQL and the app for Mac OSX
Date: 2013-06-13
Author: Michael Martinez

OSX users who develop Python applications (any application really) that use PostgreSQL are in luck. If you are looking
for, quite possibly, the easiest way to install, run and use the most advanced open source database on the planet
(provided you are using Mac OSX > 10.7). [Postgres.app](http://postgresapp.com/) | [docs](http://postgresapp.com/documentation)
- will make your life very happy. When you just want to run PostgreSQL and get to coding, Postgres.app from
[Matt Thompson](http://mattt.me/) and the awesome guys at [Heroku](http://postgres.heroku.com/) is where its at.

##Install PostgreSQL

1. Use Homebrew and follow this [guide](https://coderwall.com/p/1mni7w) or something similar
2. Use the PostgreSQL binaries and follow this [guide](http://www.enterprisedb.com/resources-community/pginst-guide)
3. Use postgres.app - it is hard to make an argument against this app. Download it, drag it to applications, DONE.

*******

##Use PostgreSQL

If you have ever used postgreSQL from the commandline you have undoubtedly felt this pain:


    :::bash
    pg_ctl -D /usr/local/var/postgres start
    pg_ctl -D /usr/local/var/postgres status
    pg_ctl -D /usr/local/var/postgres stop -s -m fast

This is just to start and/or check on the darn thing. Then you can enter the `psql` command to access the `$USER` database.
Remember that the `$USER` database doesn't have a user/password like it would in a production environment.


*******

##Use Postgres.app
The postgres app simplifies this process by allowing you to start PostgreSQL like any other mac app, click on the app.
But before you do that; Add one line to your `.bashrc` or in my case, `.zshrc`.


    :::bash
    PATH="/Applications/Postgres.app/Contents/MacOS/bin:$PATH"


Once the app initializes, you get the cool little elephant in your toolbar. That's it, PostgreSQL is running and ready to
relation. With this done you can now create a database:


    :::bash
    $ psql
    psql (9.2.2)
    Type "help" for help.

    $ michaelmartinez=# CREATE DATABASE my_database;
    # If you want to delete the database you just created
    $ michaelmartinez=# DROP DATABASE my_database;

note: don't forget the semi-colon!

*******

##Use for Development


To use this with Django you need to install the psycopg2 package, then its just a matter of adding the correct parameters
to your `DATABASE` settings:


    :::python
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "my_database",
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
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/my_database'
    db = SQLAlchemy(app)


Vanilla SQLAlchemy


    :::python
    from sqlalchemy import create_engine
    engine = create_engine('postgresql://localhost/my_database')