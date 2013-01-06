Title: Virtual Machines
Date: 2013-01-06
Author: Michael Martinez

Let me just put this right out there; Virtual Machines are awesome, but not
for me in this use case.

For the last 6 or so months I have been developing in separate environments.
Using VM ware Fusion for Mac OSX has enabled me to create virtual computers that
facilitate complete separation between my main machine and dev environments.
I will explain what I did followed by why and how it worked out.

The creation of an OSX Mountain Lion VM is painless. After creation I went in
and removed a bunch of non-necessary apps. After all, I was mainly interested in
using the VM to develop, not manage pictures or play with GarageBand. Removing
the unnecessary apps made the VM footprint a lot smaller, which was another nice
side effect.

I keep most of my important configurations in a version control system called
git. I store these repositories at Github, which makes retrieving and
subsequently installing them super easy. Once the machine was provisioned with
my configurations, I used my laptop script to install the apps and packages I
use for developing and managing.

Up to this point I have a few hours invested and I figure I can make a copy of
VM for future use. Lets call it the base VM. From here I can experiment with
new packages, modules and code. I install items without regard for my system as
I can simply roll back the changes or start anew. Life is good...

The problem I have experienced with this setup is managing what is installed,
where it is installed and how to keep track of it all. This gets really
complicated when I have 4 or 5 VM's that are purpose built for different
programming languages and/or tools. I often need to modify my path or another
config file, for example, in each VM. This is a managerial nightmare as I have
4 or 5 different dotfile configurations to stay on top of. Yuck.

What I've found is that I am unable to really stay on top of each VM and my main
machine when I really just want to focus on getting something done. Conversely,
I can't get anything done when I spend all my time making sure all of the repos
are up to date. Houston we have a problem.

My hat is off to those of you with more than one computer and also manage to
keep everything sane. I have toyed around with the idea of one main computer and
another traveling computer or something like that. This experiment has taught me
that I am a one computer man. I guess my particular OCD dictates that I keep my
config files up to date and if my computer blows up, I can simply move to another...
but not more than one at a time.
