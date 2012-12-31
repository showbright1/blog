Title: AppFog - Ruby on Rails 3.2 Tutorial
Date: 2012-06-27
Author: Michael


[AppFog][] is an incredible service in the land of PaaS or Platform as a
Service. They are a [Cloud Foundry][]-powered polyglot platform. You
can [sign up][] for beta access now and start pushing apps strait away.
Their web based management interface is really nice, and I am a sucker
for nicely designed "things."  In this post I'd like to show you all how
I got a Ruby on Rails app up and running.

Create
------

</p>
A developer has two ways to create a new RoR app.

​1. Use the AppFog console to bootstrap a shell RoR app. [[source
code][]]

This will net a basic shell RoR app with Ruby version 1.9.3-p125 and
Rails version 3.2.5

​2. Use the **af** gem to push your locally developed app to the cloud.

Push
----

</p>
How do you push an app to AppFog?

Hopefully you are using rvm, rbenv or have some sort of Ruby/Gem
management system set-up. Rvm and rbenv are out of the scope of this
tutorial. I use rvm to create project-based gemsets with a directory
level .rvmrc file. You can read more about rvm [here][].

    :::bash
    $ gem install af

When you are ready to push issue this command:

    :::bash
    $ af push <appname> --runtime=ruby193

If you don’t specify an app name, AppFog will use the directory name. I
found that my Ruby version wasn't automatically detected without the
runtime flag. I found this by looking through the af gem source code on
Github. (I love OSS!) The runtimes supported by AppFog can be found
using "af runtimes".

You will then be taken though a series of yes/no questions where the
details come into play. Accepting the default answer for all of these
questions with the exception of database technology is the simplest way
to get up and running. You can choose between Mongo and MySQL for the
database technology to use, so even that isn’t very complicated.

Let me be clear, I have not veered far from the quickest path to get my
app set-up. Subsequent tutorials will have more on this front.

Running / Errors
----------------

</p>
At this point you are either running or you have error(s). If you have
an error, use “af logs \<appname\>” to diagnose what went wrong. You can
also head to the [support forums][] or the [Google group][] to ask a
question or look through previous questions/discussions.

In either app creation case, you are going to use "af update
\<appname\>" once you have something you'd like show the world or need
to make a change. This command is strait forward; push the changes to
the cloud.

Sum it up
---------

</p>

1.  create app either on AppFog or locally
2.  install af gem
3.  af push or af update
4.  profit

</p>

### Notes:

</p>
When I looked at the available commands using "af  --help", it was not
immediately clear what each command was used for. A good option to learn
more is to read though the [source][].  OR you can wait for my next
tutorial where I'll dive in with both feet on every available command.

-------------------------------------------------------------------------

Database
--------

</p>
Using MySQL? You ***need*** the ***mysql2 gem*** in your gemfile. Also,
if you intend to develop your app against MySQL locally, you will want
your database.yml file to look like or similar to the gist below.

    :::bash
    # comment out when working locally
    # un-comment this for deployment
    development:
      adapter: sqlite3
      database: db/development.sqlite3
      pool: 5
      timeout: 5000

    # un-comment this when working locally
    # comment out when deploying
    #development:
    #  adapter: mysql2
    #  encoding: utf8
    #  reconnect: false
    #  database: gisticle_development
    #  pool: 5
    #  username: michaelmartinez
    #  password: <password>
    #  host: 127.0.0.1

    production:
      adapter: sqlite3
      database: db/production.sqlite3
      pool: 5
      timeout: 5000

I am not sure why the database.yml needs to be set-up like this and
quite frankly it could be my error (system or set-up). The error
I received was database adapter not found and I have narrowed it down to
the application creation process. Once the app is up and running, I have
been able to use either configuration.

### Notes:

</p>
Developing with MySQL locally will help to eliminate a potential source
of frustration not related to AppFog. A simple query that works with
sqlite3 may completely fail with PG or MySQL due to type casting, as
just one example. Databases like PostgreSQL and MySQL have more features
than sqlite3 but are more strict with type. So, you can avoid a lot of
potential problems by simply developing against the database you intend
to use in production.

---------------------------------------------------------------------------

Package
-------

</p>
You need to pre-package the app to the greatest extent possible.

    :::bash
    $ bundle package
    $ bundle install

Keep in mind that “bundler package” will add size, in some cases
significant size, to your app. This command caches a local version of
each gem to your vendor/cache dir and some gems are really large.

Potential problems with gems, bundler and AppFog; Lets say you need to
modify a published gem. Lets also posit that you fork and modify this
gem to fit your particular app (change color scheme, etc.). You can use
bundler's [git feature][] to host this modified gem on Github and it
will behave as if it was hosted on rubygems.org. This is great when
working locally or you have access to bundler and/or rake.

I've found that you may need to publish the modified gem to rubygems.org
for it to work properly in production. In fact I have not been able to
use un-published gems with AppFog. If your modification is a useful
feature the community may benefit from, consider submitting a pull
request through proper channels before going down this road.

### Sum it up

</p>
In a nut shell... stick with published gems and you'll be A-OK.

---------------------------------------------------------------------------

Precompile
----------

</p>
Speaking of packaging and pre-deployment. If you are using rails 3 and
the asset pipeline you need to run this command before you push or
update.

    :::bash
    $ bundle exec rake assets:precompile

---------------------------------------------------------------------------

Final Thoughts
--------------

</p>
Whew! I hope this helps you navigate the AppFog PaaS. Stay tuned for
more and if you have questions don’t hesitate to ask… in the [support
forums][] or the [Google group][]! I am neither an AppFog or
CloudFoundry expert nor an employee, I simply believe in the Kool-Aid
they are pushing.

  [AppFog]: http://www.appfog.com/
  [Cloud Foundry]: http://www.cloudfoundry.com/
  [sign up]: https://console.appfog.com/signup
  [source code]: https://github.com/appfog/af-ruby-rails
  [here]: https://rvm.io//
  [support forums]: http://support.appfog.com/forums
  [Google group]: https://groups.google.com/forum/?fromgroups#!forum/appfog-users
  [source]: https://github.com/appfog/af
  [git feature]: http://gembundler.com/git.html
