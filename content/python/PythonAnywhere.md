Title: Python Anywhere means Anywhere
Date: 2013-05-25
Author: Michael Martinez

I just signed up for the [web developer](https://www.pythonanywhere.com/pricing/) price point at [PythonAnywhere](http://pythonanywhere.com/).
PythonAnywhere is Platform as a service (PaaS) company which means they are in business to provide a platform to build from. If
you are a web developer, I am quite positive that you have heard of Heroku, Appfog and many other PaaS providers.

PythonAnywhere is a bit different in that they are not aiming to be a one stop shop for all popular language frameworks.
They are clearly attempting to lock down Python dev in the cloud. The product at PythonAnywhere is really innovative among the
PaaS companies that provide Python support as they require no local tools to be installed. They also have the notion of
file browsing for decent visual project management and editing. They also offer DropBox sync out of the box.

I particularly like that no local tools need to be installed. I can use ANY device in virtually ANY location that has
internet connectivity, HUGE! What I mean is, if I want to bang something out on my phone, tablet or my parent's 1999
HP that sounds like a jet... No problem as long as it has a decent browser and internet. This is BIG win for PythonAnywhere
and Python developers alike.

Heroku has integrated the Cloud9 webIDE and has 'management' apps for Android/iOS ([Nezumi[(http://nezumiapp.com/#/iphone)), but both are third party
projects and that can be good and bad. Appfog has no concept of File browsing, Consoles or webIDE's... I mean, they aren't
even part of the equation, but Appfog supports a ton of different frameworks/languages. I don't want to bash on Appfog,
they are a good provider and their tools are good, but PythonAnywhere has them flat out beat in some ways.

The PythonAnywhere blog actually has a more comprehensive blog post on [Heroku v. PythonAnywhere](http://blog.pythonanywhere.com/65/)
NetTuts+ has a nice comparison between [Heroku and Appfog](http://net.tutsplus.com/articles/editorials/appfog-vs-heroku/).
PythonAnywhere is based on workers and each worker has 500mb of RAM. So at $12 a month, the Web Developer account on PythonAnywhere
can have 10 webapps with 3 workers each. If you need to scale an app, I would venture to guess you could potentially
deploy more workers towards a particular app if needed (don't hold me to that). The "bang for buck" or "pound" if you
are in Britain like the founders and a Python developer is really compelling.

One can't possibly enumerate all the possibilities for using the PythonAnywhere service. From hacking basic python
scripts to running bots against irc/chat to scraping web sites/twitter to full blown web app development with Flask,
Django or any of the other [batteries included libraries/frameworks](https://www.pythonanywhere.com/batteries_included/).
The price point for this service is unheard of, but you need to be a Python developer.

Let's take a look at a static site generator, Pelican, for an example work flow... Lets say I have an idea or thought I just need to blog.
My blog is a pelican static site and I am not able to use my laptop for whatever reason. I can log into SSH into PA via
one of the many Android SSH apps (or chrome for Anroid, or ssh from vim touch), create the blog post (way slower on phone),
start a bash shell (or use the Android ZSH shell), issue a few commands and it is done. Then I commit and push via
git and/or sync to DropBox. BAM! Blog post from the cloud with a crazy web-based workflow not possible just a few years ago.

VPS are cool, but I am not a good sysadmin... I prefer coding to administration.

